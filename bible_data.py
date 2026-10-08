"""
bible_data.py
Canonical metadata for all 66 books of the Bible, including approximate dates of writing,
historical eras, authors, and a rich collection of foundational verses in KJV and WEB translations.
"""

BOOKS_METADATA = [
    # --- OLD TESTAMENT: PENTATEUCH / LAW ---
    {
        "name": "Genesis",
        "abbr": "Gen",
        "testament": "Old Testament",
        "category": "Law / Pentateuch",
        "approx_date": "c. 1446–1406 BC",
        "start_year": -1446,
        "end_year": -1406,
        "era": "Wilderness & Exodus Era",
        "author": "Moses",
        "chapters": 50
    },
    {
        "name": "Exodus",
        "abbr": "Exod",
        "testament": "Old Testament",
        "category": "Law / Pentateuch",
        "approx_date": "c. 1446–1406 BC",
        "start_year": -1446,
        "end_year": -1406,
        "era": "Wilderness & Exodus Era",
        "author": "Moses",
        "chapters": 40
    },
    {
        "name": "Leviticus",
        "abbr": "Lev",
        "testament": "Old Testament",
        "category": "Law / Pentateuch",
        "approx_date": "c. 1446–1406 BC",
        "start_year": -1446,
        "end_year": -1406,
        "era": "Wilderness & Exodus Era",
        "author": "Moses",
        "chapters": 27
    },
    {
        "name": "Numbers",
        "abbr": "Num",
        "testament": "Old Testament",
        "category": "Law / Pentateuch",
        "approx_date": "c. 1446–1406 BC",
        "start_year": -1446,
        "end_year": -1406,
        "era": "Wilderness & Exodus Era",
        "author": "Moses",
        "chapters": 36
    },
    {
        "name": "Deuteronomy",
        "abbr": "Deut",
        "testament": "Old Testament",
        "category": "Law / Pentateuch",
        "approx_date": "c. 1406 BC",
        "start_year": -1406,
        "end_year": -1406,
        "era": "Wilderness & Exodus Era",
        "author": "Moses",
        "chapters": 34
    },

    # --- OLD TESTAMENT: HISTORICAL BOOKS ---
    {
        "name": "Joshua",
        "abbr": "Josh",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 1400–1375 BC",
        "start_year": -1400,
        "end_year": -1375,
        "era": "Conquest & Judges Era",
        "author": "Joshua (attributed)",
        "chapters": 24
    },
    {
        "name": "Judges",
        "abbr": "Judg",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 1050–1000 BC",
        "start_year": -1050,
        "end_year": -1000,
        "era": "Conquest & Judges Era",
        "author": "Samuel (traditional)",
        "chapters": 21
    },
    {
        "name": "Ruth",
        "abbr": "Ruth",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 1050–1000 BC",
        "start_year": -1050,
        "end_year": -1000,
        "era": "Conquest & Judges Era",
        "author": "Samuel (traditional)",
        "chapters": 4
    },
    {
        "name": "1 Samuel",
        "abbr": "1Sam",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 930–722 BC",
        "start_year": -930,
        "end_year": -722,
        "era": "United Monarchy Era",
        "author": "Samuel / Gad / Nathan",
        "chapters": 31
    },
    {
        "name": "2 Samuel",
        "abbr": "2Sam",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 930–722 BC",
        "start_year": -930,
        "end_year": -722,
        "era": "United Monarchy Era",
        "author": "Gad / Nathan",
        "chapters": 24
    },
    {
        "name": "1 Kings",
        "abbr": "1Kgs",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 560–538 BC",
        "start_year": -560,
        "end_year": -538,
        "era": "Babylonian Exile Era",
        "author": "Jeremiah (traditional)",
        "chapters": 22
    },
    {
        "name": "2 Kings",
        "abbr": "2Kgs",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 560–538 BC",
        "start_year": -560,
        "end_year": -538,
        "era": "Babylonian Exile Era",
        "author": "Jeremiah (traditional)",
        "chapters": 25
    },
    {
        "name": "1 Chronicles",
        "abbr": "1Chr",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 450–430 BC",
        "start_year": -450,
        "end_year": -430,
        "era": "Post-Exilic / Persian Era",
        "author": "Ezra (traditional)",
        "chapters": 29
    },
    {
        "name": "2 Chronicles",
        "abbr": "2Chr",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 450–430 BC",
        "start_year": -450,
        "end_year": -430,
        "era": "Post-Exilic / Persian Era",
        "author": "Ezra (traditional)",
        "chapters": 36
    },
    {
        "name": "Ezra",
        "abbr": "Ezra",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 457–444 BC",
        "start_year": -457,
        "end_year": -444,
        "era": "Post-Exilic / Persian Era",
        "author": "Ezra",
        "chapters": 10
    },
    {
        "name": "Nehemiah",
        "abbr": "Neh",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 445–420 BC",
        "start_year": -445,
        "end_year": -420,
        "era": "Post-Exilic / Persian Era",
        "author": "Nehemiah",
        "chapters": 13
    },
    {
        "name": "Esther",
        "abbr": "Esth",
        "testament": "Old Testament",
        "category": "Historical",
        "approx_date": "c. 470–465 BC",
        "start_year": -470,
        "end_year": -465,
        "era": "Post-Exilic / Persian Era",
        "author": "Mordecai (traditional)",
        "chapters": 10
    },

    # --- OLD TESTAMENT: POETRY & WISDOM ---
    {
        "name": "Job",
        "abbr": "Job",
        "testament": "Old Testament",
        "category": "Poetry & Wisdom",
        "approx_date": "c. 2000–1800 BC (events) / c. 950 BC",
        "start_year": -2000,
        "end_year": -950,
        "era": "Patriarchal Era",
        "author": "Unknown / Job",
        "chapters": 42
    },
    {
        "name": "Psalms",
        "abbr": "Ps",
        "testament": "Old Testament",
        "category": "Poetry & Wisdom",
        "approx_date": "c. 1000–450 BC",
        "start_year": -1000,
        "end_year": -450,
        "era": "United Monarchy Era",
        "author": "David, Asaph, Sons of Korah, Moses, Solomon",
        "chapters": 150
    },
    {
        "name": "Proverbs",
        "abbr": "Prov",
        "testament": "Old Testament",
        "category": "Poetry & Wisdom",
        "approx_date": "c. 970–930 BC",
        "start_year": -970,
        "end_year": -930,
        "era": "United Monarchy Era",
        "author": "Solomon, Agur, Lemuel",
        "chapters": 31
    },
    {
        "name": "Ecclesiastes",
        "abbr": "Eccl",
        "testament": "Old Testament",
        "category": "Poetry & Wisdom",
        "approx_date": "c. 935 BC",
        "start_year": -935,
        "end_year": -935,
        "era": "United Monarchy Era",
        "author": "Solomon (Qoheleth)",
        "chapters": 12
    },
    {
        "name": "Song of Solomon",
        "abbr": "Song",
        "testament": "Old Testament",
        "category": "Poetry & Wisdom",
        "approx_date": "c. 965 BC",
        "start_year": -965,
        "end_year": -965,
        "era": "United Monarchy Era",
        "author": "Solomon",
        "chapters": 8
    },

    # --- OLD TESTAMENT: MAJOR PROPHETS ---
    {
        "name": "Isaiah",
        "abbr": "Isa",
        "testament": "Old Testament",
        "category": "Major Prophets",
        "approx_date": "c. 740–680 BC",
        "start_year": -740,
        "end_year": -680,
        "era": "Divided Kingdom Era",
        "author": "Isaiah son of Amoz",
        "chapters": 66
    },
    {
        "name": "Jeremiah",
        "abbr": "Jer",
        "testament": "Old Testament",
        "category": "Major Prophets",
        "approx_date": "c. 627–580 BC",
        "start_year": -627,
        "end_year": -580,
        "era": "Babylonian Exile Era",
        "author": "Jeremiah",
        "chapters": 52
    },
    {
        "name": "Lamentations",
        "abbr": "Lam",
        "testament": "Old Testament",
        "category": "Major Prophets",
        "approx_date": "c. 586 BC",
        "start_year": -586,
        "end_year": -586,
        "era": "Babylonian Exile Era",
        "author": "Jeremiah",
        "chapters": 5
    },
    {
        "name": "Ezekiel",
        "abbr": "Ezek",
        "testament": "Old Testament",
        "category": "Major Prophets",
        "approx_date": "c. 593–571 BC",
        "start_year": -593,
        "end_year": -571,
        "era": "Babylonian Exile Era",
        "author": "Ezekiel",
        "chapters": 48
    },
    {
        "name": "Daniel",
        "abbr": "Dan",
        "testament": "Old Testament",
        "category": "Major Prophets",
        "approx_date": "c. 605–530 BC",
        "start_year": -605,
        "end_year": -530,
        "era": "Babylonian Exile Era",
        "author": "Daniel",
        "chapters": 12
    },

    # --- OLD TESTAMENT: MINOR PROPHETS ---
    {
        "name": "Hosea",
        "abbr": "Hos",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 750–715 BC",
        "start_year": -750,
        "end_year": -715,
        "era": "Divided Kingdom Era",
        "author": "Hosea",
        "chapters": 14
    },
    {
        "name": "Joel",
        "abbr": "Joel",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 835–796 BC",
        "start_year": -835,
        "end_year": -796,
        "era": "Divided Kingdom Era",
        "author": "Joel",
        "chapters": 3
    },
    {
        "name": "Amos",
        "abbr": "Amos",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 760–750 BC",
        "start_year": -760,
        "end_year": -750,
        "era": "Divided Kingdom Era",
        "author": "Amos",
        "chapters": 9
    },
    {
        "name": "Obadiah",
        "abbr": "Obad",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 586 BC",
        "start_year": -586,
        "end_year": -586,
        "era": "Babylonian Exile Era",
        "author": "Obadiah",
        "chapters": 1
    },
    {
        "name": "Jonah",
        "abbr": "Jonah",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 780–760 BC",
        "start_year": -780,
        "end_year": -760,
        "era": "Divided Kingdom Era",
        "author": "Jonah",
        "chapters": 4
    },
    {
        "name": "Micah",
        "abbr": "Mic",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 735–700 BC",
        "start_year": -735,
        "end_year": -700,
        "era": "Divided Kingdom Era",
        "author": "Micah",
        "chapters": 7
    },
    {
        "name": "Nahum",
        "abbr": "Nah",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 663–612 BC",
        "start_year": -663,
        "end_year": -612,
        "era": "Divided Kingdom Era",
        "author": "Nahum",
        "chapters": 3
    },
    {
        "name": "Habakkuk",
        "abbr": "Hab",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 612–598 BC",
        "start_year": -612,
        "end_year": -598,
        "era": "Divided Kingdom Era",
        "author": "Habakkuk",
        "chapters": 3
    },
    {
        "name": "Zephaniah",
        "abbr": "Zeph",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 635–625 BC",
        "start_year": -635,
        "end_year": -625,
        "era": "Divided Kingdom Era",
        "author": "Zephaniah",
        "chapters": 3
    },
    {
        "name": "Haggai",
        "abbr": "Hag",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 520 BC",
        "start_year": -520,
        "end_year": -520,
        "era": "Post-Exilic / Persian Era",
        "author": "Haggai",
        "chapters": 2
    },
    {
        "name": "Zechariah",
        "abbr": "Zech",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 520–480 BC",
        "start_year": -520,
        "end_year": -480,
        "era": "Post-Exilic / Persian Era",
        "author": "Zechariah",
        "chapters": 14
    },
    {
        "name": "Malachi",
        "abbr": "Mal",
        "testament": "Old Testament",
        "category": "Minor Prophets",
        "approx_date": "c. 433–424 BC",
        "start_year": -433,
        "end_year": -424,
        "era": "Post-Exilic / Persian Era",
        "author": "Malachi",
        "chapters": 4
    },

    # --- NEW TESTAMENT: GOSPELS & ACTS ---
    {
        "name": "Matthew",
        "abbr": "Matt",
        "testament": "New Testament",
        "category": "Gospels",
        "approx_date": "c. 60–70 AD",
        "start_year": 60,
        "end_year": 70,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Matthew (Levi)",
        "chapters": 28
    },
    {
        "name": "Mark",
        "abbr": "Mark",
        "testament": "New Testament",
        "category": "Gospels",
        "approx_date": "c. 55–65 AD",
        "start_year": 55,
        "end_year": 65,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "John Mark",
        "chapters": 16
    },
    {
        "name": "Luke",
        "abbr": "Luke",
        "testament": "New Testament",
        "category": "Gospels",
        "approx_date": "c. 60–62 AD",
        "start_year": 60,
        "end_year": 62,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Luke the Physician",
        "chapters": 24
    },
    {
        "name": "John",
        "abbr": "John",
        "testament": "New Testament",
        "category": "Gospels",
        "approx_date": "c. 85–95 AD",
        "start_year": 85,
        "end_year": 95,
        "era": "Late 1st Century AD",
        "author": "John the Apostle",
        "chapters": 21
    },
    {
        "name": "Acts",
        "abbr": "Acts",
        "testament": "New Testament",
        "category": "Acts / Church History",
        "approx_date": "c. 62–64 AD",
        "start_year": 62,
        "end_year": 64,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Luke the Physician",
        "chapters": 28
    },

    # --- NEW TESTAMENT: PAULINE EPISTLES ---
    {
        "name": "Romans",
        "abbr": "Rom",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 57 AD",
        "start_year": 57,
        "end_year": 57,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 16
    },
    {
        "name": "1 Corinthians",
        "abbr": "1Cor",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 55 AD",
        "start_year": 55,
        "end_year": 55,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 16
    },
    {
        "name": "2 Corinthians",
        "abbr": "2Cor",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 56 AD",
        "start_year": 56,
        "end_year": 56,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 13
    },
    {
        "name": "Galatians",
        "abbr": "Gal",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 48–49 AD",
        "start_year": 48,
        "end_year": 49,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 6
    },
    {
        "name": "Ephesians",
        "abbr": "Eph",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 60–62 AD",
        "start_year": 60,
        "end_year": 62,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 6
    },
    {
        "name": "Philippians",
        "abbr": "Phil",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 61–62 AD",
        "start_year": 61,
        "end_year": 62,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 4
    },
    {
        "name": "Colossians",
        "abbr": "Col",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 60–62 AD",
        "start_year": 60,
        "end_year": 62,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 4
    },
    {
        "name": "1 Thessalonians",
        "abbr": "1Thess",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 50–51 AD",
        "start_year": 50,
        "end_year": 51,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 5
    },
    {
        "name": "2 Thessalonians",
        "abbr": "2Thess",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 51–52 AD",
        "start_year": 51,
        "end_year": 52,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 3
    },
    {
        "name": "1 Timothy",
        "abbr": "1Tim",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 62–64 AD",
        "start_year": 62,
        "end_year": 64,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 6
    },
    {
        "name": "2 Timothy",
        "abbr": "2Tim",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 66–67 AD",
        "start_year": 66,
        "end_year": 67,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 4
    },
    {
        "name": "Titus",
        "abbr": "Titus",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 63–65 AD",
        "start_year": 63,
        "end_year": 65,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 3
    },
    {
        "name": "Philemon",
        "abbr": "Phlm",
        "testament": "New Testament",
        "category": "Pauline Epistles",
        "approx_date": "c. 60–62 AD",
        "start_year": 60,
        "end_year": 62,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Paul the Apostle",
        "chapters": 1
    },

    # --- NEW TESTAMENT: GENERAL EPISTLES ---
    {
        "name": "Hebrews",
        "abbr": "Heb",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 64–69 AD",
        "start_year": 64,
        "end_year": 69,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Unknown (Paul / Apollos / Barnabas)",
        "chapters": 13
    },
    {
        "name": "James",
        "abbr": "Jas",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 45–48 AD",
        "start_year": 45,
        "end_year": 48,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "James (brother of Jesus)",
        "chapters": 5
    },
    {
        "name": "1 Peter",
        "abbr": "1Pet",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 63–64 AD",
        "start_year": 63,
        "end_year": 64,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Peter the Apostle",
        "chapters": 5
    },
    {
        "name": "2 Peter",
        "abbr": "2Pet",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 65–68 AD",
        "start_year": 65,
        "end_year": 68,
        "era": "Apostolic & Early Church (1st Century AD)",
        "author": "Peter the Apostle",
        "chapters": 3
    },
    {
        "name": "1 John",
        "abbr": "1John",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 85–95 AD",
        "start_year": 85,
        "end_year": 95,
        "era": "Late 1st Century AD",
        "author": "John the Apostle",
        "chapters": 5
    },
    {
        "name": "2 John",
        "abbr": "2John",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 85–95 AD",
        "start_year": 85,
        "end_year": 95,
        "era": "Late 1st Century AD",
        "author": "John the Apostle",
        "chapters": 1
    },
    {
        "name": "3 John",
        "abbr": "3John",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 85–95 AD",
        "start_year": 85,
        "end_year": 95,
        "era": "Late 1st Century AD",
        "author": "John the Apostle",
        "chapters": 1
    },
    {
        "name": "Jude",
        "abbr": "Jude",
        "testament": "New Testament",
        "category": "General Epistles",
        "approx_date": "c. 65–80 AD",
        "start_year": 65,
        "end_year": 80,
        "era": "Late 1st Century AD",
        "author": "Jude (brother of James and Jesus)",
        "chapters": 1
    },

    # --- NEW TESTAMENT: APOCALYPTIC ---
    {
        "name": "Revelation",
        "abbr": "Rev",
        "testament": "New Testament",
        "category": "Apocalyptic",
        "approx_date": "c. 95–96 AD",
        "start_year": 95,
        "end_year": 96,
        "era": "Late 1st Century AD",
        "author": "John the Apostle",
        "chapters": 22
    }
]

TRANSLATIONS = {
    "KJV": "King James Version (KJV)",
    "WEB": "World English Bible (WEB)"
}

# A curated dataset containing representative, inspirational, and foundational verses
# spanning all 66 books in both King James Version (KJV) and World English Bible (WEB).
SEEDED_VERSES = [
    # --- GENESIS ---
    {
        "book": "Genesis", "chapter": 1, "verse": 1,
        "kjv": "In the beginning God created the heaven and the earth.",
        "web": "In the beginning, God created the heavens and the earth."
    },
    {
        "book": "Genesis", "chapter": 1, "verse": 3,
        "kjv": "And God said, Let there be light: and there was light.",
        "web": "God said, \"Let there be light,\" and there was light."
    },
    {
        "book": "Genesis", "chapter": 1, "verse": 27,
        "kjv": "So God created man in his own image, in the image of God created he him; male and female created he them.",
        "web": "God created man in his own image. In God's image he created him; male and female he created them."
    },
    {
        "book": "Genesis", "chapter": 12, "verse": 2,
        "kjv": "And I will make of thee a great nation, and I will bless thee, and make thy name great; and thou shalt be a blessing.",
        "web": "I will make of you a great nation. I will bless you and make your name great. You will be a blessing."
    },
    {
        "book": "Genesis", "chapter": 50, "verse": 20,
        "kjv": "But as for you, ye thought evil against me; but God meant it unto good, to bring to pass, as it is this day, to save much people alive.",
        "web": "As for you, you meant evil against me, but God meant it for good, to bring to pass, as it is today, to save many people alive."
    },

    # --- EXODUS ---
    {
        "book": "Exodus", "chapter": 3, "verse": 14,
        "kjv": "And God said unto Moses, I AM THAT I AM: and he said, Thus shalt thou say unto the children of Israel, I AM hath sent me unto you.",
        "web": "God said to Moses, \"I AM WHO I AM,\" and he said, \"You shall tell the children of Israel this: 'I AM has sent me to you.'\""
    },
    {
        "book": "Exodus", "chapter": 14, "verse": 14,
        "kjv": "The LORD shall fight for you, and ye shall hold your peace.",
        "web": "Yahweh will fight for you, and you shall be still."
    },
    {
        "book": "Exodus", "chapter": 20, "verse": 3,
        "kjv": "Thou shalt have no other gods before me.",
        "web": "You shall have no other gods before me."
    },

    # --- LEVITICUS ---
    {
        "book": "Leviticus", "chapter": 19, "verse": 18,
        "kjv": "Thou shalt not avenge, nor bear any grudge against the children of thy people, but thou shalt love thy neighbour as thyself: I am the LORD.",
        "web": "You shall not take vengeance, nor bear any grudge against the children of your people; but you shall love your neighbor as yourself. I am Yahweh."
    },
    {
        "book": "Leviticus", "chapter": 20, "verse": 26,
        "kjv": "And ye shall be holy unto me: for I the LORD am holy, and have severed you from other people, that ye should be mine.",
        "web": "You shall be holy to me; for I, Yahweh, am holy, and have set you apart from the peoples, that you should be mine."
    },

    # --- NUMBERS ---
    {
        "book": "Numbers", "chapter": 6, "verse": 24,
        "kjv": "The LORD bless thee, and keep thee:",
        "web": "Yahweh bless you, and keep you."
    },
    {
        "book": "Numbers", "chapter": 6, "verse": 25,
        "kjv": "The LORD make his face shine upon thee, and be gracious unto thee:",
        "web": "Yahweh make his face to shine on you, and be gracious to you."
    },
    {
        "book": "Numbers", "chapter": 6, "verse": 26,
        "kjv": "The LORD lift up his countenance upon thee, and give thee peace.",
        "web": "Yahweh lift up his face toward you, and give you peace."
    },

    # --- DEUTERONOMY ---
    {
        "book": "Deuteronomy", "chapter": 6, "verse": 4,
        "kjv": "Hear, O Israel: The LORD our God is one LORD:",
        "web": "Hear, Israel: Yahweh is our God. Yahweh is one."
    },
    {
        "book": "Deuteronomy", "chapter": 6, "verse": 5,
        "kjv": "And thou shalt love the LORD thy God with all thine heart, and with all thy soul, and with all thy might.",
        "web": "You shall love Yahweh your God with all your heart, with all your soul, and with all your might."
    },
    {
        "book": "Deuteronomy", "chapter": 31, "verse": 6,
        "kjv": "Be strong and of a good courage, fear not, nor be afraid of them: for the LORD thy God, he it is that doth go with thee; he will not fail thee, nor forsake thee.",
        "web": "Be strong and courageous. Don't be afraid, nor be scared of them; for Yahweh your God is who goes with you. He will not fail you nor forsake you."
    },

    # --- JOSHUA ---
    {
        "book": "Joshua", "chapter": 1, "verse": 9,
        "kjv": "Have not I commanded thee? Be strong and of a good courage; be not afraid, neither be thou dismayed: for the LORD thy God is with thee whithersoever thou goest.",
        "web": "Haven't I commanded you? Be strong and courageous. Don't be afraid. Don't be dismayed, for Yahweh your God is with you wherever you go."
    },
    {
        "book": "Joshua", "chapter": 24, "verse": 15,
        "kjv": "And if it seem evil unto you to serve the LORD, choose you this day whom ye will serve; but as for me and my house, we will serve the LORD.",
        "web": "If it seems evil to you to serve Yahweh, choose today whom you will serve; but as for me and my house, we will serve Yahweh."
    },

    # --- JUDGES ---
    {
        "book": "Judges", "chapter": 5, "verse": 31,
        "kjv": "So let all thine enemies perish, O LORD: but let them that love him be as the sun when he goeth forth in his might.",
        "web": "So let all your enemies perish, Yahweh, but let those who love him be like the sun when it rises in its strength."
    },

    # --- RUTH ---
    {
        "book": "Ruth", "chapter": 1, "verse": 16,
        "kjv": "And Ruth said, Intreat me not to leave thee, or to return from following after thee: for whither thou goest, I will go; and where thou lodgest, I will lodge: thy people shall be my people, and thy God my God:",
        "web": "Ruth said, \"Don't urge me to leave you, and to return from following after you, for where you go, I will go; and where you stay, I will stay. Your people will be my people, and your God my God.\""
    },

    # --- 1 SAMUEL ---
    {
        "book": "1 Samuel", "chapter": 16, "verse": 7,
        "kjv": "For the LORD seeth not as man seeth; for man looketh on the outward appearance, but the LORD looketh on the heart.",
        "web": "For Yahweh sees not as man sees; for man looks at the outward appearance, but Yahweh looks at the heart."
    },

    # --- 2 SAMUEL ---
    {
        "book": "2 Samuel", "chapter": 22, "verse": 3,
        "kjv": "The God of my rock; in him will I trust: he is my shield, and the horn of my salvation, my high tower, and my refuge, my saviour; thou savest me from violence.",
        "web": "My God, my rock, in him I will take refuge; my shield, and the horn of my salvation, my high tower, and my refuge. My savior, you save me from violence."
    },

    # --- 1 KINGS ---
    {
        "book": "1 Kings", "chapter": 19, "verse": 12,
        "kjv": "And after the earthquake a fire; but the LORD was not in the fire: and after the fire a still small voice.",
        "web": "After the earthquake, a fire; but Yahweh was not in the fire. After the fire, a still small voice."
    },

    # --- 2 KINGS ---
    {
        "book": "2 Kings", "chapter": 6, "verse": 16,
        "kjv": "And he answered, Fear not: for they that be with us are more than they that be with them.",
        "web": "He answered, \"Don't be afraid; for those who are with us are more than those who are with them.\""
    },

    # --- 1 CHRONICLES ---
    {
        "book": "1 Chronicles", "chapter": 16, "verse": 34,
        "kjv": "O give thanks unto the LORD; for he is good; for his mercy endureth for ever.",
        "web": "Oh give thanks to Yahweh, for he is good, for his loving kindness endures forever."
    },

    # --- 2 CHRONICLES ---
    {
        "book": "2 Chronicles", "chapter": 7, "verse": 14,
        "kjv": "If my people, which are called by my name, shall humble themselves, and pray, and seek my face, and turn from their wicked ways; then will I hear from heaven, and will forgive their sin, and will heal their land.",
        "web": "If my people, who are called by my name, will humble themselves, pray, seek my face, and turn from their wicked ways; then I will hear from heaven, will forgive their sin, and will heal their land."
    },

    # --- EZRA ---
    {
        "book": "Ezra", "chapter": 7, "verse": 10,
        "kjv": "For Ezra had prepared his heart to seek the law of the LORD, and to do it, and to teach in Israel statutes and judgments.",
        "web": "For Ezra had set his heart to seek Yahweh's law, and to do it, and to teach statutes and ordinances in Israel."
    },

    # --- NEHEMIAH ---
    {
        "book": "Nehemiah", "chapter": 8, "verse": 10,
        "kjv": "Then he said unto them, Go your way, eat the fat, and drink the sweet, and send portions unto them for whom nothing is prepared: for this day is holy unto our Lord: neither be ye sorry; for the joy of the LORD is your strength.",
        "web": "Then he said to them, \"Go your way. Eat the fat, drink the sweet, and send portions to him for whom nothing is prepared; for this day is holy to our Lord. Don't be grieved; for the joy of Yahweh is your strength.\""
    },

    # --- ESTHER ---
    {
        "book": "Esther", "chapter": 4, "verse": 14,
        "kjv": "And who knoweth whether thou art come to the kingdom for such a time as this?",
        "web": "Who knows whether you haven't come to the kingdom for such a time as this?"
    },

    # --- JOB ---
    {
        "book": "Job", "chapter": 19, "verse": 25,
        "kjv": "For I know that my redeemer liveth, and that he shall stand at the latter day upon the earth:",
        "web": "But as for me, I know that my Redeemer lives. In the end, he will stand upon the earth."
    },

    # --- PSALMS ---
    {
        "book": "Psalms", "chapter": 23, "verse": 1,
        "kjv": "The LORD is my shepherd; I shall not want.",
        "web": "Yahweh is my shepherd: I shall lack nothing."
    },
    {
        "book": "Psalms", "chapter": 23, "verse": 4,
        "kjv": "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me.",
        "web": "Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me. Your rod and your staff, they comfort me."
    },
    {
        "book": "Psalms", "chapter": 46, "verse": 1,
        "kjv": "God is our refuge and strength, a very present help in trouble.",
        "web": "God is our refuge and strength, a very present help in trouble."
    },
    {
        "book": "Psalms", "chapter": 46, "verse": 10,
        "kjv": "Be still, and know that I am God: I will be exalted among the heathen, I will be exalted in the earth.",
        "web": "Be still, and know that I am God. I will be exalted among the nations. I will be exalted in the earth."
    },
    {
        "book": "Psalms", "chapter": 119, "verse": 105,
        "kjv": "Thy word is a lamp unto my feet, and a light unto my path.",
        "web": "Your word is a lamp to my feet, and a light for my path."
    },
    {
        "book": "Psalms", "chapter": 121, "verse": 2,
        "kjv": "My help cometh from the LORD, which made heaven and earth.",
        "web": "My help comes from Yahweh, who made heaven and earth."
    },

    # --- PROVERBS ---
    {
        "book": "Proverbs", "chapter": 3, "verse": 5,
        "kjv": "Trust in the LORD with all thine heart; and lean not unto thine own understanding.",
        "web": "Trust in Yahweh with all your heart, and don't lean on your own understanding."
    },
    {
        "book": "Proverbs", "chapter": 3, "verse": 6,
        "kjv": "In all thy ways acknowledge him, and he shall direct thy paths.",
        "web": "In all your ways acknowledge him, and he will make your paths straight."
    },
    {
        "book": "Proverbs", "chapter": 18, "verse": 10,
        "kjv": "The name of the LORD is a strong tower: the righteous runneth into it, and is safe.",
        "web": "Yahweh's name is a strong tower: the righteous run to him, and are safe."
    },

    # --- ECCLESIASTES ---
    {
        "book": "Ecclesiastes", "chapter": 3, "verse": 1,
        "kjv": "To every thing there is a season, and a time to every purpose under the heaven:",
        "web": "For everything there is a season, and a time for every purpose under heaven:"
    },
    {
        "book": "Ecclesiastes", "chapter": 3, "verse": 11,
        "kjv": "He hath made every thing beautiful in his time: also he hath set the world in their heart, so that no man can find out the work that God maketh from the beginning to the end.",
        "web": "He has made everything beautiful in its time. He has also set eternity in their hearts, yet so that man can't find out the work that God has done from the beginning even to the end."
    },

    # --- SONG OF SOLOMON ---
    {
        "book": "Song of Solomon", "chapter": 2, "verse": 16,
        "kjv": "My beloved is mine, and I am his: he feedeth among the lilies.",
        "web": "My beloved is mine, and I am his. He browses among the lilies."
    },

    # --- ISAIAH ---
    {
        "book": "Isaiah", "chapter": 9, "verse": 6,
        "kjv": "For unto us a child is born, unto us a son is given: and the government shall be upon his shoulder: and his name shall be called Wonderful, Counsellor, The mighty God, The everlasting Father, The Prince of Peace.",
        "web": "For to us a child is born. To us a son is given; and the government will be on his shoulders. His name will be called Wonderful, Counselor, Mighty God, Everlasting Father, Prince of Peace."
    },
    {
        "book": "Isaiah", "chapter": 40, "verse": 31,
        "kjv": "But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint.",
        "web": "But those who wait for Yahweh will renew their strength. They will mount up with wings like eagles. They will run, and not be weary. They will walk, and not faint."
    },
    {
        "book": "Isaiah", "chapter": 41, "verse": 10,
        "kjv": "Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.",
        "web": "Don't you be afraid, for I am with you. Don't be dismayed, for I am your God. I will strengthen you. Yes, I will help you. Yes, I will uphold you with the right hand of my righteousness."
    },
    {
        "book": "Isaiah", "chapter": 53, "verse": 5,
        "kjv": "But he was wounded for our transgressions, he was bruised for our iniquities: the chastisement of our peace was upon him; and with his stripes we are healed.",
        "web": "But he was pierced for our transgressions. He was crushed for our iniquities. The punishment that brought our peace was on him; and by his wounds we are healed."
    },

    # --- JEREMIAH ---
    {
        "book": "Jeremiah", "chapter": 29, "verse": 11,
        "kjv": "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.",
        "web": "For I know the thoughts that I think toward you, says Yahweh, thoughts of peace, and not of evil, to give you hope and a future."
    },
    {
        "book": "Jeremiah", "chapter": 33, "verse": 3,
        "kjv": "Call unto me, and I will answer thee, and shew thee great and mighty things, which thou knowest not.",
        "web": "Call to me, and I will answer you, and will show you great and difficult things, which you don't know."
    },

    # --- LAMENTATIONS ---
    {
        "book": "Lamentations", "chapter": 3, "verse": 22,
        "kjv": "It is of the LORD's mercies that we are not consumed, because his compassions fail not.",
        "web": "It is because of Yahweh's loving kindnesses that we are not consumed, because his compassion doesn't fail."
    },
    {
        "book": "Lamentations", "chapter": 3, "verse": 23,
        "kjv": "They are new every morning: great is thy faithfulness.",
        "web": "They are new every morning. Great is your faithfulness."
    },

    # --- EZEKIEL ---
    {
        "book": "Ezekiel", "chapter": 36, "verse": 26,
        "kjv": "A new heart also will I give you, and a new spirit will I put within you: and I will take away the stony heart out of your flesh, and I will give you an heart of flesh.",
        "web": "I will also give you a new heart, and I will put a new spirit within you. I will take away the stony heart out of your flesh, and I will give you a heart of flesh."
    },

    # --- DANIEL ---
    {
        "book": "Daniel", "chapter": 12, "verse": 3,
        "kjv": "And they that be wise shall shine as the brightness of the firmament; and they that turn many to righteousness as the stars for ever and ever.",
        "web": "Those who are wise will shine as the brightness of the expanse. Those who turn many to righteousness will shine as the stars forever and ever."
    },

    # --- HOSEA ---
    {
        "book": "Hosea", "chapter": 6, "verse": 6,
        "kjv": "For I desired mercy, and not sacrifice; and the knowledge of God more than burnt offerings.",
        "web": "For I desire mercy, and not sacrifice; and the knowledge of God more than burnt offerings."
    },

    # --- JOEL ---
    {
        "book": "Joel", "chapter": 2, "verse": 28,
        "kjv": "And it shall come to pass afterward, that I will pour out my spirit upon all flesh; and your sons and your daughters shall prophesy, your old men shall dream dreams, your young men shall see visions:",
        "web": "It will happen afterward, that I will pour out my Spirit on all flesh; and your sons and your daughters will prophesy. Your old men will dream dreams. Your young men will see visions."
    },

    # --- AMOS ---
    {
        "book": "Amos", "chapter": 5, "verse": 24,
        "kjv": "But let judgment run down as waters, and righteousness as a mighty stream.",
        "web": "But let justice roll on like rivers, and righteousness like a mighty stream."
    },

    # --- OBADIAH ---
    {
        "book": "Obadiah", "chapter": 1, "verse": 15,
        "kjv": "For the day of the LORD is near upon all the heathen: as thou hast done, it shall be done unto thee: thy reward shall return upon thine own head.",
        "web": "For the day of Yahweh is near on all the nations! As you have done, it will be done to you. Your deed will return upon your own head."
    },

    # --- JONAH ---
    {
        "book": "Jonah", "chapter": 2, "verse": 9,
        "kjv": "But I will sacrifice unto thee with the voice of thanksgiving; I will pay that that I have vowed. Salvation is of the LORD.",
        "web": "But I will sacrifice to you with the voice of thanksgiving. I will pay that which I have vowed. Salvation belongs to Yahweh."
    },

    # --- MICAH ---
    {
        "book": "Micah", "chapter": 6, "verse": 8,
        "kjv": "He hath shewed thee, O man, what is good; and what doth the LORD require of thee, but to do justly, and to love mercy, and to walk humbly with thy God?",
        "web": "He has shown you, O man, what is good. What does Yahweh require of you, but to act justly, to love mercy, and to walk humbly with your God?"
    },

    # --- NAHUM ---
    {
        "book": "Nahum", "chapter": 1, "verse": 7,
        "kjv": "The LORD is good, a strong hold in the day of trouble; and he knoweth them that trust in him.",
        "web": "Yahweh is good, a stronghold in the day of trouble; and he knows those who take refuge in him."
    },

    # --- HABAKKUK ---
    {
        "book": "Habakkuk", "chapter": 3, "verse": 19,
        "kjv": "The LORD God is my strength, and he will make my feet like hinds' feet, and he will make me to walk upon mine high places.",
        "web": "Yahweh, the Lord, is my strength. He makes my feet like deer's feet, and enables me to go in high places."
    },

    # --- ZEPHANIAH ---
    {
        "book": "Zephaniah", "chapter": 3, "verse": 17,
        "kjv": "The LORD thy God in the midst of thee is mighty; he will save, he will rejoice over thee with joy; he will rest in his love, he will joy over thee with singing.",
        "web": "Yahweh, your God, is among you, a mighty one who will save. He will rejoice over you with joy. He will calm you in his love. He will rejoice over you with singing."
    },

    # --- HAGGAI ---
    {
        "book": "Haggai", "chapter": 2, "verse": 9,
        "kjv": "The glory of this latter house shall be greater than of the former, saith the LORD of hosts: and in this place will I give peace, saith the LORD of hosts.",
        "web": "\"The latter glory of this house will be greater than the former,\" says Yahweh of Armies; \"and in this place I will give peace,\" says Yahweh of Armies."
    },

    # --- ZECHARIAH ---
    {
        "book": "Zechariah", "chapter": 4, "verse": 6,
        "kjv": "Then he answered and spake unto me, saying, This is the word of the LORD unto Zerubbabel, saying, Not by might, nor by power, but by my spirit, saith the LORD of hosts.",
        "web": "Then he answered and spoke to me, saying, \"This is Yahweh's word to Zerubbabel, saying: 'Not by might, nor by power, but by my Spirit,' says Yahweh of Armies.\""
    },

    # --- MALACHI ---
    {
        "book": "Malachi", "chapter": 4, "verse": 2,
        "kjv": "But unto you that fear my name shall the Sun of righteousness arise with healing in his wings; and ye shall go forth, and grow up as calves of the stall.",
        "web": "But to you who fear my name shall the sun of righteousness arise with healing in its wings. You will go out, and leap like calves of the stall."
    },

    # --- MATTHEW ---
    {
        "book": "Matthew", "chapter": 5, "verse": 14,
        "kjv": "Ye are the light of the world. A city that is set on an hill cannot be hid.",
        "web": "You are the light of the world. A city located on a hill can't be hidden."
    },
    {
        "book": "Matthew", "chapter": 5, "verse": 16,
        "kjv": "Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven.",
        "web": "Even so, let your light shine before men, that they may see your good works, and glorify your Father who is in heaven."
    },
    {
        "book": "Matthew", "chapter": 6, "verse": 33,
        "kjv": "But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.",
        "web": "But seek first God's Kingdom and his righteousness; and all these things will be given to you as well."
    },
    {
        "book": "Matthew", "chapter": 11, "verse": 28,
        "kjv": "Come unto me, all ye that labour and are heavy laden, and I will give you rest.",
        "web": "Come to me, all you who labor and are heavily burdened, and I will give you rest."
    },
    {
        "book": "Matthew", "chapter": 28, "verse": 19,
        "kjv": "Go ye therefore, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost:",
        "web": "Go and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit,"
    },

    # --- MARK ---
    {
        "book": "Mark", "chapter": 10, "verse": 27,
        "kjv": "And Jesus looking upon them saith, With men it is impossible, but not with God: for with God all things are possible.",
        "web": "Jesus, looking at them, said, \"With men it is impossible, but not with God, for all things are possible with God.\""
    },
    {
        "book": "Mark", "chapter": 12, "verse": 30,
        "kjv": "And thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy mind, and with all thy strength: this is the first commandment.",
        "web": "You shall love the Lord your God with all your heart, with all your soul, with all your mind, and with all your strength. This is the first commandment."
    },

    # --- LUKE ---
    {
        "book": "Luke", "chapter": 1, "verse": 37,
        "kjv": "For with God nothing shall be impossible.",
        "web": "For nothing is impossible with God."
    },
    {
        "book": "Luke", "chapter": 2, "verse": 14,
        "kjv": "Glory to God in the highest, and on earth peace, good will toward men.",
        "web": "Glory to God in the highest, on earth peace, good will toward men."
    },
    {
        "book": "Luke", "chapter": 19, "verse": 10,
        "kjv": "For the Son of man is come to seek and to save that which was lost.",
        "web": "For the Son of Man came to seek and to save that which was lost."
    },

    # --- JOHN ---
    {
        "book": "John", "chapter": 1, "verse": 1,
        "kjv": "In the beginning was the Word, and the Word was with God, and the Word was God.",
        "web": "In the beginning was the Word, and the Word was with God, and the Word was God."
    },
    {
        "book": "John", "chapter": 3, "verse": 16,
        "kjv": "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.",
        "web": "For God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life."
    },
    {
        "book": "John", "chapter": 8, "verse": 12,
        "kjv": "Then spake Jesus again unto them, saying, I am the light of the world: he that followeth me shall not walk in darkness, but shall have the light of life.",
        "web": "Again, therefore, Jesus spoke to them, saying, \"I am the light of the world. He who follows me will not walk in the darkness, but will have the light of life.\""
    },
    {
        "book": "John", "chapter": 14, "verse": 6,
        "kjv": "Jesus saith unto him, I am the way, the truth, and the life: no man cometh unto the Father, but by me.",
        "web": "Jesus said to him, \"I am the way, the truth, and the life. No one comes to the Father, except through me.\""
    },
    {
        "book": "John", "chapter": 14, "verse": 27,
        "kjv": "Peace I leave with you, my peace I give unto you: not as the world giveth, give I unto you. Let not your heart be troubled, neither let it be afraid.",
        "web": "Peace I leave with you. My peace I give to you; not as the world gives, give I to you. Don't let your heart be troubled, neither let it be fearful."
    },

    # --- ACTS ---
    {
        "book": "Acts", "chapter": 1, "verse": 8,
        "kjv": "But ye shall receive power, after that the Holy Ghost is come upon you: and ye shall be witnesses unto me both in Jerusalem, and in all Judaea, and in Samaria, and unto the uttermost part of the earth.",
        "web": "But you will receive power when the Holy Spirit has come upon you. You will be witnesses to me in Jerusalem, in all Judea and Samaria, and to the uttermost parts of the earth."
    },
    {
        "book": "Acts", "chapter": 4, "verse": 12,
        "kjv": "Neither is there salvation in any other: for there is none other name under heaven given among men, whereby we must be saved.",
        "web": "There is salvation in no one else, for there is no other name under heaven that is given among men, by which we must be saved!"
    },

    # --- ROMANS ---
    {
        "book": "Romans", "chapter": 8, "verse": 28,
        "kjv": "And we know that all things work together for good to them that love God, to them who are the called according to his purpose.",
        "web": "We know that all things work together for good for those who love God, for those who are called according to his purpose."
    },
    {
        "book": "Romans", "chapter": 8, "verse": 38,
        "kjv": "For I am persuaded, that neither death, nor life, nor angels, nor principalities, nor powers, nor things present, nor things to come,",
        "web": "For I am persuaded, that neither death, nor life, nor angels, nor principalities, nor things present, nor things to come,"
    },
    {
        "book": "Romans", "chapter": 8, "verse": 39,
        "kjv": "Nor height, nor depth, nor any other creature, shall be able to separate us from the love of God, which is in Christ Jesus our Lord.",
        "web": "nor height, nor depth, nor any other created thing, will be able to separate us from God's love, which is in Christ Jesus our Lord."
    },
    {
        "book": "Romans", "chapter": 12, "verse": 2,
        "kjv": "And be not conformed to this world: but be ye transformed by the renewing of your mind, that ye may prove what is that good, and acceptable, and perfect, will of God.",
        "web": "Don't be conformed to this world, but be transformed by the renewing of your mind, so that you may prove what is the good, well-pleasing, and perfect will of God."
    },

    # --- 1 CORINTHIANS ---
    {
        "book": "1 Corinthians", "chapter": 13, "verse": 4,
        "kjv": "Charity suffereth long, and is kind; charity envieth not; charity vaunteth not itself, is not puffed up,",
        "web": "Love is patient and is kind; love doesn't envy. Love doesn't brag, is not proud,"
    },
    {
        "book": "1 Corinthians", "chapter": 13, "verse": 13,
        "kjv": "And now abideth faith, hope, charity, these three; but the greatest of these is charity.",
        "web": "But now faith, hope, and love remain—these three. The greatest of these is love."
    },

    # --- 2 CORINTHIANS ---
    {
        "book": "2 Corinthians", "chapter": 5, "verse": 17,
        "kjv": "Therefore if any man be in Christ, he is a new creature: old things are passed away; behold, all things are become new.",
        "web": "Therefore if anyone is in Christ, he is a new creation. The old things have passed away. Behold, all things have become new."
    },
    {
        "book": "2 Corinthians", "chapter": 12, "verse": 9,
        "kjv": "And he said unto me, My grace is sufficient for thee: for my strength is made perfect in weakness. Most gladly therefore will I rather glory in my infirmities, that the power of Christ may rest upon me.",
        "web": "He has said to me, \"My grace is sufficient for you, for my power is made perfect in weakness.\" Most gladly therefore I will rather glory in my weaknesses, that the power of Christ may rest on me."
    },

    # --- GALATIANS ---
    {
        "book": "Galatians", "chapter": 2, "verse": 20,
        "kjv": "I am crucified with Christ: nevertheless I live; yet not I, but Christ liveth in me: and the life which I now live in the flesh I live by the faith of the Son of God, who loved me, and gave himself for me.",
        "web": "I have been crucified with Christ, and it is no longer I that live, but Christ lives in me. That life which I now live in the flesh, I live by faith in the Son of God, who loved me, and gave himself up for me."
    },
    {
        "book": "Galatians", "chapter": 5, "verse": 22,
        "kjv": "But the fruit of the Spirit is love, joy, peace, longsuffering, gentleness, goodness, faith,",
        "web": "But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness,"
    },
    {
        "book": "Galatians", "chapter": 5, "verse": 23,
        "kjv": "Meekness, temperance: against such there is no law.",
        "web": "gentleness, and self-control. Against such things there is no law."
    },

    # --- EPHESIANS ---
    {
        "book": "Ephesians", "chapter": 2, "verse": 8,
        "kjv": "For by grace are ye saved through faith; and that not of yourselves: it is the gift of God:",
        "web": "For by grace you have been saved through faith, and that not of yourselves; it is the gift of God,"
    },
    {
        "book": "Ephesians", "chapter": 2, "verse": 9,
        "kjv": "Not of works, lest any man should boast.",
        "web": "not of works, that no one would boast."
    },
    {
        "book": "Ephesians", "chapter": 6, "verse": 10,
        "kjv": "Finally, my brethren, be strong in the Lord, and in the power of his might.",
        "web": "Finally, be strong in the Lord, and in the strength of his might."
    },

    # --- PHILIPPIANS ---
    {
        "book": "Philippians", "chapter": 4, "verse": 6,
        "kjv": "Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God.",
        "web": "In nothing be anxious, but in everything, by prayer and petition with thanksgiving, let your requests be made known to God."
    },
    {
        "book": "Philippians", "chapter": 4, "verse": 7,
        "kjv": "And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus.",
        "web": "And the peace of God, which surpasses all understanding, will guard your hearts and your thoughts in Christ Jesus."
    },
    {
        "book": "Philippians", "chapter": 4, "verse": 13,
        "kjv": "I can do all things through Christ which strengtheneth me.",
        "web": "I can do all things through Christ, who strengthens me."
    },

    # --- COLOSSIANS ---
    {
        "book": "Colossians", "chapter": 3, "verse": 12,
        "kjv": "Put on therefore, as the elect of God, holy and beloved, bowels of mercies, kindness, humbleness of mind, meekness, longsuffering;",
        "web": "Put on therefore, as God's chosen ones, holy and beloved, a heart of compassion, kindness, lowliness, humility, and perseverance;"
    },
    {
        "book": "Colossians", "chapter": 3, "verse": 23,
        "kjv": "And whatsoever ye do, do it heartily, as to the Lord, and not unto men;",
        "web": "Whatever you do, work at it with all your heart, as working for the Lord, and not for men,"
    },

    # --- 1 THESSALONIANS ---
    {
        "book": "1 Thessalonians", "chapter": 5, "verse": 16,
        "kjv": "Rejoice evermore.",
        "web": "Rejoice always."
    },
    {
        "book": "1 Thessalonians", "chapter": 5, "verse": 17,
        "kjv": "Pray without ceasting.",
        "web": "Pray without ceasing."
    },
    {
        "book": "1 Thessalonians", "chapter": 5, "verse": 18,
        "kjv": "In every thing give thanks: for this is the will of God in Christ Jesus concerning you.",
        "web": "In everything give thanks, for this is the will of God in Christ Jesus toward you."
    },

    # --- 2 THESSALONIANS ---
    {
        "book": "2 Thessalonians", "chapter": 3, "verse": 3,
        "kjv": "But the Lord is faithful, who shall stablish you, and keep you from evil.",
        "web": "But the Lord is faithful, who will establish you and guard you from the evil one."
    },

    # --- 1 TIMOTHY ---
    {
        "book": "1 Timothy", "chapter": 6, "verse": 6,
        "kjv": "But godliness with contentment is great gain.",
        "web": "But godliness with contentment is great gain."
    },
    {
        "book": "1 Timothy", "chapter": 6, "verse": 12,
        "kjv": "Fight the good fight of faith, lay hold on eternal life, whereunto thou art also called, and hast professed a good profession before many witnesses.",
        "web": "Fight the good fight of faith. Lay hold on the eternal life to which you were called, and you confessed the good confession in the sight of many witnesses."
    },

    # --- 2 TIMOTHY ---
    {
        "book": "2 Timothy", "chapter": 1, "verse": 7,
        "kjv": "For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind.",
        "web": "For God didn't give us a spirit of fear, but of power, love, and self-control."
    },
    {
        "book": "2 Timothy", "chapter": 3, "verse": 16,
        "kjv": "All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness:",
        "web": "Every Scripture is God-breathed and profitable for teaching, for reproof, for correction, and for instruction in righteousness,"
    },

    # --- TITUS ---
    {
        "book": "Titus", "chapter": 2, "verse": 11,
        "kjv": "For the grace of God that bringeth salvation hath appeared to all men,",
        "web": "For the grace of God has appeared, bringing salvation to all men,"
    },

    # --- PHILEMON ---
    {
        "book": "Philemon", "chapter": 1, "verse": 4,
        "kjv": "I thank my God, making mention of thee always in my prayers,",
        "web": "I thank my God always, making mention of you in my prayers,"
    },

    # --- HEBREWS ---
    {
        "book": "Hebrews", "chapter": 11, "verse": 1,
        "kjv": "Now faith is the substance of things hoped for, the evidence of things not seen.",
        "web": "Now faith is assurance of things hoped for, proof of things not seen."
    },
    {
        "book": "Hebrews", "chapter": 12, "verse": 1,
        "kjv": "Wherefore seeing we also are compassed about with so great a cloud of witnesses, let us lay aside every weight, and the sin which doth so easily beset us, and let us run with patience the race that is set before us,",
        "web": "Therefore let's also, seeing we are surrounded by so great a cloud of witnesses, lay aside every weight and the sin which so easily entangles us, and let's run with perseverance the race that is set before us,"
    },
    {
        "book": "Hebrews", "chapter": 12, "verse": 2,
        "kjv": "Looking unto Jesus the author and finisher of our faith; who for the joy that was set before him endured the cross, despising the shame, and is set down at the right hand of the throne of God.",
        "web": "looking to Jesus, the author and perfecter of faith, who for the joy that was set before him endured the cross, despising its shame, and has sat down at the right hand of the throne of God."
    },

    # --- JAMES ---
    {
        "book": "James", "chapter": 1, "verse": 2,
        "kjv": "My brethren, count it all joy when ye fall into divers temptations;",
        "web": "Count it all joy, my brothers, when you fall into various temptations,"
    },
    {
        "book": "James", "chapter": 1, "verse": 5,
        "kjv": "If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him.",
        "web": "But if any of you lacks wisdom, let him ask of God, who gives to all liberally and without reproach; and it will be given to him."
    },

    # --- 1 PETER ---
    {
        "book": "1 Peter", "chapter": 5, "verse": 7,
        "kjv": "Casting all your care upon him; for he careeth for you.",
        "web": "casting all your worries on him, because he cares for you."
    },

    # --- 2 PETER ---
    {
        "book": "2 Peter", "chapter": 3, "verse": 9,
        "kjv": "The Lord is not slack concerning his promise, as some men count slackness; but is longsuffering to us-ward, not willing that any should perish, but that all should come to repentance.",
        "web": "The Lord is not slow concerning his promise, as some count slowness; but is patient with us, not wishing that any should perish, but that all should come to repentance."
    },

    # --- 1 JOHN ---
    {
        "book": "1 John", "chapter": 1, "verse": 9,
        "kjv": "If we confess our sins, he is faithful and just to forgive us our sins, and to cleanse us from all unrighteousness.",
        "web": "If we confess our sins, he is faithful and righteous to forgive us our sins, and to cleanse us from all unrighteousness."
    },
    {
        "book": "1 John", "chapter": 4, "verse": 7,
        "kjv": "Beloved, let us love one another: for love is of God; and every one that loveth is born of God, and knoweth God.",
        "web": "Beloved, let's love one another, for love is of God; and everyone who loves has been born of God, and knows God."
    },
    {
        "book": "1 John", "chapter": 4, "verse": 8,
        "kjv": "He that loveth not knoweth not God; for God is love.",
        "web": "He who doesn't love doesn't know God, for God is love."
    },

    # --- 2 JOHN ---
    {
        "book": "2 John", "chapter": 1, "verse": 6,
        "kjv": "And this is love, that we walk after his commandments. This is the commandment, That, as ye have heard from the beginning, ye should walk in it.",
        "web": "This is love, that we should walk according to his commandments. This is the commandment, even as you heard from the beginning, that you should walk in it."
    },

    # --- 3 JOHN ---
    {
        "book": "3 John", "chapter": 1, "verse": 4,
        "kjv": "I have no greater joy than to hear that my children walk in truth.",
        "web": "I have no greater joy than this: to hear about my children walking in truth."
    },

    # --- JUDE ---
    {
        "book": "Jude", "chapter": 1, "verse": 24,
        "kjv": "Now unto him that is able to keep you from falling, and to present you faultless before the presence of his glory with exceeding joy,",
        "web": "Now to him who is able to keep them from stumbling, and to present you faultless before the presence of his glory in great joy,"
    },
    {
        "book": "Jude", "chapter": 1, "verse": 25,
        "kjv": "To the only wise God our Saviour, be glory and majesty, dominion and power, both now and ever. Amen.",
        "web": "to God our Savior, who alone is wise, be glory and majesty, dominion and power, both now and forever. Amen."
    },

    # --- REVELATION ---
    {
        "book": "Revelation", "chapter": 1, "verse": 8,
        "kjv": "I am Alpha and Omega, the beginning and the ending, saith the Lord, which is, and which was, and which is to come, the Almighty.",
        "web": "\"I am the Alpha and the Omega, the Beginning and the End,\" says the Lord God, \"who is and who was and who is to come, the Almighty.\""
    },
    {
        "book": "Revelation", "chapter": 3, "verse": 20,
        "kjv": "Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I will come in to him, and will sup with him, and he with me.",
        "web": "Behold, I stand at the door and knock. If anyone hears my voice and opens the door, then I will come in to him, and will dine with him, and he with me."
    },
    {
        "book": "Revelation", "chapter": 21, "verse": 4,
        "kjv": "And God shall wipe away all tears from their eyes; and there shall be no more death, neither sorrow, nor crying, neither shall there be any more pain: for the former things are passed away.",
        "web": "He will wipe away every tear from their eyes. Death will be no more; neither will there be mourning, nor crying, nor pain, any more. The first things have passed away."
    },
    {
        "book": "Revelation", "chapter": 22, "verse": 20,
        "kjv": "He which testifieth these things saith, Surely I come quickly. Amen. Even so, come, Lord Jesus.",
        "web": "He who testifies these things says, \"Yes, I come quickly.\" Amen! Yes, come, Lord Jesus."
    }
]
