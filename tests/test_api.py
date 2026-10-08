"""
tests/test_api.py
Automated test suite verifying the Flask API endpoints, database operations,
random verse generation, and multi-dimensional search capabilities.
"""

import unittest
import json
import os
import sys

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
import database

class BibleAppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        cls.client = app.test_client()
        # Initialize DB in case it isn't yet
        database.init_db()

    def test_homepage(self):
        """Verify the single-page application loads with status 200."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.data.decode("utf-8")
        self.assertIn("Scripture Chronos", html)
        self.assertIn("Historical Context & Chronology", html)

    def test_random_verse_structure(self):
        """Verify /api/random returns all requested metadata fields."""
        response = self.client.get("/api/random")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["status"], "success")

        v = data["verse"]
        # Required attributes check:
        self.assertIn("book", v)
        self.assertIn("chapter", v)
        self.assertIn("verse", v)
        self.assertIn("reference", v)
        self.assertIn("translation", v)
        self.assertIn("translation_name", v)
        self.assertIn("approx_date_written", v)
        self.assertIn("era", v)
        self.assertIn("text", v)
        self.assertTrue(len(v["text"]) > 0)
        self.assertTrue(len(v["approx_date_written"]) > 0)

    def test_random_verse_filters(self):
        """Verify /api/random respects translation and testament filters."""
        # Translation filter
        res_kjv = self.client.get("/api/random?translation=KJV")
        self.assertEqual(res_kjv.status_code, 200)
        v_kjv = json.loads(res_kjv.data)["verse"]
        self.assertEqual(v_kjv["translation"], "KJV")

        res_web = self.client.get("/api/random?translation=WEB")
        self.assertEqual(res_web.status_code, 200)
        v_web = json.loads(res_web.data)["verse"]
        self.assertEqual(v_web["translation"], "WEB")

        # Testament filter
        res_ot = self.client.get("/api/random?testament=Old%20Testament")
        self.assertEqual(res_ot.status_code, 200)
        v_ot = json.loads(res_ot.data)["verse"]
        self.assertEqual(v_ot["testament"], "Old Testament")

        res_nt = self.client.get("/api/random?testament=New%20Testament")
        self.assertEqual(res_nt.status_code, 200)
        v_nt = json.loads(res_nt.data)["verse"]
        self.assertEqual(v_nt["testament"], "New Testament")

    def test_search_by_text(self):
        """Verify searching by text keyword returns matching verses."""
        response = self.client.get("/api/search?q=light")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["status"], "success")
        self.assertGreater(data["total"], 0)
        # Check that matched results contain 'light' (case-insensitive) in text or attributes
        has_light = any("light" in v["text"].lower() for v in data["verses"])
        self.assertTrue(has_light)

    def test_search_by_book(self):
        """Verify searching by book name."""
        response = self.client.get("/api/search?book=Genesis")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(data["total"], 0)
        for v in data["verses"]:
            self.assertEqual(v["book"], "Genesis")

    def test_search_by_chapter_and_verse(self):
        """Verify searching by chapter and verse number."""
        response = self.client.get("/api/search?chapter=3&verse=16")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(data["total"], 0)
        for v in data["verses"]:
            self.assertEqual(v["chapter"], 3)
            self.assertEqual(v["verse"], 16)

    def test_search_by_translation(self):
        """Verify searching and filtering by translation."""
        response = self.client.get("/api/search?translation=KJV&book=Romans")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(data["total"], 0)
        for v in data["verses"]:
            self.assertEqual(v["translation"], "KJV")

    def test_search_by_approximate_time_written(self):
        """Verify searching by historical approximate date written."""
        # Search by date keyword e.g. "57 AD" (Romans composition)
        response = self.client.get("/api/search?time=57%20AD")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(data["total"], 0)
        for v in data["verses"]:
            self.assertIn("57 AD", v["approx_date_written"])

        # Search by BC
        res_bc = self.client.get("/api/search?time=BC")
        self.assertEqual(res_bc.status_code, 200)
        data_bc = json.loads(res_bc.data)
        self.assertGreater(data_bc["total"], 0)
        for v in data_bc["verses"]:
            self.assertIn("BC", v["approx_date_written"])

    def test_search_by_era(self):
        """Verify searching by historical era."""
        response = self.client.get("/api/search?era=Wilderness")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(data["total"], 0)
        for v in data["verses"]:
            self.assertIn("Wilderness", v["era"])

    def test_omni_search_reference_parsing(self):
        """Verify omni-search handles references like 'John 3:16' seamlessly."""
        response = self.client.get("/api/search?q=John%203:16")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreater(data["total"], 0)
        for v in data["verses"]:
            self.assertEqual(v["book"], "John")
            self.assertEqual(v["chapter"], 3)
            self.assertEqual(v["verse"], 16)

    def test_metadata_endpoint(self):
        """Verify /api/metadata returns canonical books, eras, translations, and categories."""
        response = self.client.get("/api/metadata")
        self.assertEqual(response.status_code, 200)
        meta = json.loads(response.data)["metadata"]
        self.assertEqual(len(meta["books"]), 66)  # All 66 books!
        self.assertGreater(len(meta["eras"]), 0)
        self.assertGreater(len(meta["translations"]), 0)
        self.assertIn("Old Testament", meta["testaments"])
        self.assertIn("New Testament", meta["testaments"])

    def test_verse_by_id_endpoint(self):
        """Verify /api/verse/<id> returns specific verse and navigation links."""
        # Fetch verse id 1
        response = self.client.get("/api/verse/1")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["verse"]["id"], 1)
        self.assertIsNotNone(data["verse"]["text"])

        # Nonexistent verse returns 404
        bad_response = self.client.get("/api/verse/999999")
        self.assertEqual(bad_response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
