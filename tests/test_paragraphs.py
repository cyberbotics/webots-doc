"""Test module for the paragraphs."""

import unittest
import re

from books import Books


class TestParagraphs(unittest.TestCase):
    """Unit test of the MD files."""

    def setUp(self):
        """Setup: get all the paragraphs."""
        self.paragraphs = []
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                with open(md_path) as f:
                    content = f.read()
                for match in re.finditer(r'(?s)((?:[^\n][\n]?)+)', content):
                    paragraph = content[match.start():match.end() - 1]
                    self.paragraphs.append(paragraph)
        # for p in self.paragraphs:
        #     print '@@@'
        #     print paragraph
        #     print '@@@'

    def test_something(self):
        """TODO."""
        pass
