# Scripture Chronos: Bible Verse & Chronology Explorer

A clean, responsive web application built with **Plain Vanilla JavaScript**, **HTML5**, **CSS3**, and **Python Flask** that displays random Bible verses alongside full biblical references, translations, and approximate historical dates of writing, with multi-dimensional search capabilities across all of those attributes.

---

## Features

- **Random Bible Verse Display**:
  - Displays random verses on demand (or with keyboard shortcut <kbd>Space</kbd>).
  - Can restrict random picks by Testament (Old / New) or Translation (KJV / WEB).
- **Full Biblical Reference & Metadata**:
  - **Book**, **Chapter**, and **Verse Number** (e.g., *Genesis 1:1*, *Romans 8:28*).
  - **Bible Translation**: Distinct badges for *King James Version (KJV)* and *World English Bible (WEB)*.
  - **Approximate Time Written**: Historical composition date (e.g., *c. 1446–1406 BC*, *c. 57 AD*).
  - **Historical Era**: Categorized by biblical timeline (e.g., *Wilderness & Exodus Era*, *United Monarchy Era*, *Babylonian Exile Era*, *Apostolic & Early Church*).
  - **Author & Literary Category**: Displays traditional author and biblical division.
- **Multi-Dimensional Search**:
  - **Omni-Search Bar**: A single search box that instantly matches across:
    - Verse text keywords / phrases (e.g., `"light"`, `"peace"`, `"love is patient"`).
    - Biblical reference format (e.g., `"John 3:16"`, `"Romans 8:28"`).
    - Book name (e.g., `"Genesis"`, `"Psalms"`).
    - Historical date / era (e.g., `"50 AD"`, `"1400 BC"`, `"Exile"`).
    - Translation (e.g., `"KJV"`, `"WEB"`).
  - **Advanced Filters Drawer**:
    - Dedicated Book dropdown (all 66 canonical books).
    - Chapter & Verse number inputs.
    - Translation dropdown.
    - Historical Era dropdown.
    - Approximate Date Written input.
- **Frontend Usability**:
  - **100% Vanilla JavaScript**: Zero external UI framework dependencies.
  - **Light & Dark Theme**: Toggle between warm parchment and obsidian themes, saved to `localStorage`.
  - **One-Click Copy**: Copies formatted scripture with full reference, translation, and historical date to clipboard.
  - **Keyboard Shortcuts**:
    - <kbd>Space</kbd>: Roll a new random verse.
    - <kbd>/</kbd>: Focus the search bar.
    - <kbd>Esc</kbd>: Clear search and return to random view.
  - **Responsive Design**: Optimized for mobile, tablet, and desktop screens.

---

## Directory Structure

```
bible_verses/
├── app.py                  # Flask web server & REST API
├── database.py             # SQLite database layer, schema, seeding, & search
├── bible_data.py           # Canonical 66-book chronology & verses dataset
├── bible.db                # SQLite database (auto-generated on startup)
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css       # Responsive styling & themes
│   └── js/
│       └── app.js          # Vanilla JavaScript logic & interactions
├── templates/
│   └── index.html          # Semantic HTML5 layout
└── tests/
    └── test_api.py         # Automated test suite (12 unit tests)
```

---

## How to Run

### 1. Install Dependencies
```bash
py -3.9 -m pip install -r requirements.txt
```

### 2. Start the Flask Server
```bash
py -3.9 app.py
```
Open your browser to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 3. Run Automated Tests
```bash
py -3.9 -m unittest discover -s tests -v
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the single-page application UI |
| `GET` | `/api/random` | Returns a random verse (supports `?translation=`, `?testament=`, `?book=`, `?era=`) |
| `GET` | `/api/search` | Multi-dimensional search (`?q=`, `?book=`, `?chapter=`, `?verse=`, `?translation=`, `?time=`, `?era=`) |
| `GET` | `/api/metadata` | Returns all 66 books, historical eras, translations, and categories |
| `GET` | `/api/verse/<id>` | Retrieves a specific verse with adjacent previous/next verse navigation IDs |
