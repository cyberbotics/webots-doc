"""Test module for the titles."""

import unittest
import re

from books import Books


class TestTitles(unittest.TestCase):
    """Unit test of the titles."""

    def setUp(self):
        """Setup: get all the titles."""
        self.titles = []
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                # Extract MD content.
                with open(md_path) as f:
                    content = f.read()

                # Remove annoying string sequences.
                # - Multiline code sections.
                content = re.sub(r'```.*```', '', content, flags=re.S)

                # Extract titles.
                for match in re.finditer(r'(#+ .*)', content):
                    title = content[match.start():match.end()]
                    self.titles.append(title)
        # Debug: Uncomment to display all the acquired titles.
        # for t in self.titles:
        #     print (t)

    def test_underscores_are_protected(self):
        """Test that titles doesn't contain any unprotected underscore."""
        for t in self.titles:
            self.assertTrue(
                re.search(r'[^\\]_', t) is None,
                msg='Title "%s" contains unprotected underscore(s).' % t
            )
