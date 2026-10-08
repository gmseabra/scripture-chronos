"""
app.py
Flask Application for Bible Verse Randomizer & Multi-Dimensional Search.
Serves the web UI and provides RESTful endpoints.
"""

import os
from flask import Flask, render_template, request, jsonify
import database

app = Flask(__name__)

# Ensure database is initialized before handling requests
with app.app_context():
    database.init_db()

@app.route("/")
def index():
    """Serves the main single-page application interface."""
    return render_template("index.html")

@app.route("/api/random", methods=["GET"])
def api_random_verse():
    """Returns a random verse matching optional filters."""
    filters = {
        "translation": request.args.get("translation"),
        "book": request.args.get("book"),
        "testament": request.args.get("testament"),
        "era": request.args.get("era")
    }
    # Clean out empty strings
    filters = {k: v for k, v in filters.items() if v and v.strip()}

    verse = database.get_random_verse(filters=filters)
    if verse:
        return jsonify({"status": "success", "verse": verse})
    return jsonify({
        "status": "error",
        "message": "No verse found matching the selected criteria."
    }), 404

@app.route("/api/search", methods=["GET"])
def api_search_verses():
    """
    Searches verses across any metadata dimension:
    - q (omni-search for text, reference, translation, or era)
    - book
    - chapter
    - verse
    - translation
    - time (approximate date written)
    - era
    - testament
    - category
    """
    q = request.args.get("q")
    book = request.args.get("book")
    chapter = request.args.get("chapter")
    verse_num = request.args.get("verse")
    translation = request.args.get("translation")
    time_query = request.args.get("time")
    era = request.args.get("era")
    testament = request.args.get("testament")
    category = request.args.get("category")

    limit = request.args.get("limit", default=50, type=int)
    offset = request.args.get("offset", default=0, type=int)

    # Cap limit to 200 for performance
    limit = min(max(1, limit), 200)
    offset = max(0, offset)

    results = database.search_verses(
        q=q,
        book=book,
        chapter=chapter,
        verse=verse_num,
        translation=translation,
        time_query=time_query,
        era=era,
        testament=testament,
        category=category,
        limit=limit,
        offset=offset
    )

    return jsonify({
        "status": "success",
        "total": results["total"],
        "limit": results["limit"],
        "offset": results["offset"],
        "verses": results["verses"]
    })

@app.route("/api/metadata", methods=["GET"])
def api_metadata():
    """Returns all books, eras, translations, categories, and testaments for UI filters."""
    meta = database.get_metadata()
    return jsonify({
        "status": "success",
        "metadata": meta
    })

@app.route("/api/verse/<int:verse_id>", methods=["GET"])
def api_get_verse(verse_id):
    """Returns details for a specific verse by ID."""
    verse = database.get_verse_by_id(verse_id)
    if verse:
        return jsonify({"status": "success", "verse": verse})
    return jsonify({
        "status": "error",
        "message": f"Verse with ID {verse_id} not found."
    }), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
