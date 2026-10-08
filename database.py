"""
database.py
Database layer for Bible Verse Randomizer & Search Application.
Provides SQLite initialization, data seeding, and flexible multi-criteria search.
"""

import sqlite3
import os
import re
from bible_data import BOOKS_METADATA, TRANSLATIONS, SEEDED_VERSES

DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bible.db")

def get_db_connection(db_path=None):
    if db_path is None:
        db_path = DEFAULT_DB_PATH
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path=None):
    """Initializes the database schema and populates canonical metadata and verses."""
    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            abbr TEXT NOT NULL,
            testament TEXT NOT NULL,
            category TEXT NOT NULL,
            approx_date_written TEXT NOT NULL,
            start_year INTEGER,
            end_year INTEGER,
            era TEXT NOT NULL,
            author TEXT,
            chapters INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS verses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            book_name TEXT NOT NULL,
            chapter INTEGER NOT NULL,
            verse INTEGER NOT NULL,
            translation TEXT NOT NULL,
            translation_name TEXT NOT NULL,
            text TEXT NOT NULL,
            FOREIGN KEY (book_id) REFERENCES books (id)
        )
    """)

    # Indexes for fast querying and filtering
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_book ON verses (book_name)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_ref ON verses (book_name, chapter, verse)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_verses_trans ON verses (translation)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_books_era ON books (era)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_books_testament ON books (testament)")

    # Check if books need seeding
    cursor.execute("SELECT COUNT(*) FROM books")
    book_count = cursor.fetchone()[0]
    if book_count == 0:
        for b in BOOKS_METADATA:
            cursor.execute("""
                INSERT INTO books (name, abbr, testament, category, approx_date_written, start_year, end_year, era, author, chapters)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                b["name"], b["abbr"], b["testament"], b["category"],
                b["approx_date"], b["start_year"], b["end_year"],
                b["era"], b["author"], b["chapters"]
            ))

    # Check if verses need seeding
    cursor.execute("SELECT COUNT(*) FROM verses")
    verse_count = cursor.fetchone()[0]
    if verse_count == 0:
        # Build book_id lookup map
        cursor.execute("SELECT id, name FROM books")
        book_id_map = {row["name"]: row["id"] for row in cursor.fetchall()}

        for v in SEEDED_VERSES:
            b_name = v["book"]
            b_id = book_id_map.get(b_name)
            if not b_id:
                continue

            # Insert KJV
            if "kjv" in v:
                cursor.execute("""
                    INSERT INTO verses (book_id, book_name, chapter, verse, translation, translation_name, text)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (b_id, b_name, v["chapter"], v["verse"], "KJV", TRANSLATIONS["KJV"], v["kjv"]))

            # Insert WEB
            if "web" in v:
                cursor.execute("""
                    INSERT INTO verses (book_id, book_name, chapter, verse, translation, translation_name, text)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (b_id, b_name, v["chapter"], v["verse"], "WEB", TRANSLATIONS["WEB"], v["web"]))

    conn.commit()
    conn.close()

def parse_reference_query(q):
    """
    Attempts to parse reference patterns from user input like:
    'John 3:16', 'Genesis 1:1', '1 John 4:8', 'Ps 23', 'Romans 8'
    Returns tuple: (parsed_book, parsed_chapter, parsed_verse) or None
    """
    if not q:
        return None, None, None
    q = q.strip()
    pattern = r'^(?:(\d\s+[A-Za-z]+|[A-Za-z]+))\s+(\d+)(?::(\d+))?$'
    match = re.match(pattern, q)
    if match:
        book_candidate = match.group(1)
        chapter_candidate = int(match.group(2))
        verse_candidate = int(match.group(3)) if match.group(3) else None
        return book_candidate, chapter_chapter_candidate_safe(chapter_candidate), verse_candidate
    return None, None, None

def chapter_chapter_candidate_safe(ch):
    return ch

def get_random_verse(filters=None, db_path=None):
    """Retrieves a single random verse matching any optional filter criteria."""
    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    sql = """
        SELECT
            v.id,
            v.book_name,
            v.chapter,
            v.verse,
            v.translation,
            v.translation_name,
            v.text,
            b.approx_date_written,
            b.era,
            b.testament,
            b.category,
            b.author
        FROM verses v
        JOIN books b ON v.book_id = b.id
        WHERE 1=1
    """
    params = []
    if filters:
        if filters.get("translation"):
            sql += " AND v.translation = ?"
            params.append(filters["translation"].strip().upper())
        if filters.get("book"):
            sql += " AND (v.book_name = ? OR b.abbr = ?)"
            params.extend([filters["book"].strip(), filters["book"].strip()])
        if filters.get("testament"):
            sql += " AND b.testament = ?"
            params.append(filters["testament"].strip())
        if filters.get("era"):
            sql += " AND b.era LIKE ?"
            params.append(f"%{filters['era'].strip()}%")

    sql += " ORDER BY RANDOM() LIMIT 1"
    cursor.execute(sql, params)
    row = cursor.fetchone()
    conn.close()

    if row:
        return format_verse_row(row)
    return None

def search_verses(
    q=None,
    book=None,
    chapter=None,
    verse=None,
    translation=None,
    time_query=None,
    era=None,
    testament=None,
    category=None,
    limit=50,
    offset=0,
    db_path=None
):
    """
    Multi-dimensional search across:
    - Text (keywords, phrases)
    - Reference: Book name, Chapter number, Verse number
    - Translation (e.g., KJV, WEB)
    - Approximate Time Written (e.g., '1400 BC', '50 AD', '1st Century')
    - Era, Testament, Author, Category
    """
    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    conditions = []
    params = []

    # 1. Omni-query parsing (if user types e.g. "John 3:16", "Romans 8:28", or free text)
    if q and q.strip():
        q_clean = q.strip()
        ref_book, ref_ch, ref_v = parse_reference_query(q_clean)

        if ref_book and ref_ch:
            # Matched a structured reference like "John 3:16" or "Genesis 1"
            ref_cond = "(v.book_name LIKE ? AND v.chapter = ?"
            params.extend([f"%{ref_book}%", ref_ch])
            if ref_v is not None:
                ref_cond += " AND v.verse = ?"
                params.append(ref_v)
            ref_cond += ")"
            conditions.append(ref_cond)
        else:
            # Omni-search matching across:
            # - Verse text
            # - Book name or abbreviation
            # - Translation
            # - Approximate date written
            # - Historical era
            # - Author
            # - Category
            omni_cond = """(
                v.text LIKE ?
                OR v.book_name LIKE ?
                OR b.abbr LIKE ?
                OR v.translation LIKE ?
                OR v.translation_name LIKE ?
                OR b.approx_date_written LIKE ?
                OR b.era LIKE ?
                OR b.author LIKE ?
                OR b.category LIKE ?
            )"""
            term = f"%{q_clean}%"
            conditions.append(omni_cond)
            params.extend([term] * 9)

    # 2. Specific filter criteria
    if book and book.strip():
        conditions.append("(v.book_name LIKE ? OR b.abbr LIKE ?)")
        params.extend([f"%{book.strip()}%", f"%{book.strip()}%"])

    if chapter is not None and str(chapter).strip() != "":
        try:
            ch_num = int(chapter)
            conditions.append("v.chapter = ?")
            params.append(ch_num)
        except ValueError:
            pass

    if verse is not None and str(verse).strip() != "":
        try:
            v_num = int(verse)
            conditions.append("v.verse = ?")
            params.append(v_num)
        except ValueError:
            pass

    if translation and translation.strip():
        trans_clean = translation.strip().upper()
        conditions.append("(v.translation = ? OR v.translation_name LIKE ?)")
        params.extend([trans_clean, f"%{translation.strip()}%"])

    if time_query and time_query.strip():
        t_term = f"%{time_query.strip()}%"
        conditions.append("(b.approx_date_written LIKE ? OR b.era LIKE ?)")
        params.extend([t_term, t_term])

    if era and era.strip():
        conditions.append("b.era LIKE ?")
        params.append(f"%{era.strip()}%")

    if testament and testament.strip():
        conditions.append("b.testament = ?")
        params.append(testament.strip())

    if category and category.strip():
        conditions.append("b.category LIKE ?")
        params.append(f"%{category.strip()}%")

    where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""

    # Count total matches
    count_sql = f"""
        SELECT COUNT(*)
        FROM verses v
        JOIN books b ON v.book_id = b.id
        {where_clause}
    """
    cursor.execute(count_sql, params)
    total = cursor.fetchone()[0]

    # Retrieve page of verses
    select_sql = f"""
        SELECT
            v.id,
            v.book_name,
            v.chapter,
            v.verse,
            v.translation,
            v.translation_name,
            v.text,
            b.approx_date_written,
            b.era,
            b.testament,
            b.category,
            b.author
        FROM verses v
        JOIN books b ON v.book_id = b.id
        {where_clause}
        ORDER BY b.id ASC, v.chapter ASC, v.verse ASC, v.translation ASC
        LIMIT ? OFFSET ?
    """
    page_params = params + [limit, offset]
    cursor.execute(select_sql, page_params)
    rows = cursor.fetchall()
    conn.close()

    results = [format_verse_row(r) for r in rows]
    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "verses": results
    }

def get_verse_by_id(verse_id, db_path=None):
    """Retrieves a single verse by ID with adjacent verse navigation."""
    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            v.id,
            v.book_name,
            v.chapter,
            v.verse,
            v.translation,
            v.translation_name,
            v.text,
            b.approx_date_written,
            b.era,
            b.testament,
            b.category,
            b.author
        FROM verses v
        JOIN books b ON v.book_id = b.id
        WHERE v.id = ?
    """, (verse_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return None

    verse_data = format_verse_row(row)

    # Find previous verse in same translation
    cursor.execute("""
        SELECT id FROM verses
        WHERE translation = ? AND id < ?
        ORDER BY id DESC LIMIT 1
    """, (row["translation"], verse_id))
    prev_row = cursor.fetchone()
    verse_data["prev_id"] = prev_row[0] if prev_row else None

    # Find next verse in same translation
    cursor.execute("""
        SELECT id FROM verses
        WHERE translation = ? AND id > ?
        ORDER BY id ASC LIMIT 1
    """, (row["translation"], verse_id))
    next_row = cursor.fetchone()
    verse_data["next_id"] = next_row[0] if next_row else None

    conn.close()
    return verse_data

def get_metadata(db_path=None):
    """Returns all books, eras, translations, categories, and testaments for UI filters."""
    conn = get_db_connection(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, abbr, testament, category, approx_date_written, era, author, chapters
        FROM books
        ORDER BY id ASC
    """)
    books = [dict(r) for r in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT era FROM books ORDER BY id ASC")
    eras = [r["era"] for r in cursor.fetchall() if r["era"]]

    cursor.execute("SELECT DISTINCT translation, translation_name FROM verses ORDER BY translation ASC")
    translations = [{"code": r["translation"], "name": r["translation_name"]} for r in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT category FROM books ORDER BY id ASC")
    categories = [r["category"] for r in cursor.fetchall() if r["category"]]

    conn.close()
    return {
        "books": books,
        "eras": eras,
        "translations": translations,
        "categories": categories,
        "testaments": ["Old Testament", "New Testament"]
    }

def format_verse_row(row):
    """Formats a database row into a structured dictionary."""
    return {
        "id": row["id"],
        "book": row["book_name"],
        "chapter": row["chapter"],
        "verse": row["verse"],
        "reference": f"{row['book_name']} {row['chapter']}:{row['verse']}",
        "translation": row["translation"],
        "translation_name": row["translation_name"],
        "text": row["text"],
        "approx_date_written": row["approx_date_written"],
        "era": row["era"],
        "testament": row["testament"],
        "category": row["category"],
        "author": row["author"]
    }
