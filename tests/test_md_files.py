"""Test module of the MD files."""
import unittest
from books import Books

import os


class TestMDFiles(unittest.TestCase):
    """Unit test of the MD files."""

    def test_md_files_are_existing(self):
        """Test that the MD files are existing."""
        books = Books()
        self.assertGreater(len(books.books), 0, msg='No books found')
        for book in books.books:
            self.assertGreater(
                len(book.md_paths), 0,
                msg='No MD files found in book "%s"' % book
            )
            for md_filename in book.md_paths:
                self.assertTrue(
                    os.path.isfile(md_filename),
                    msg='MD file "%s" is not existing' % (md_filename)
                )
                with open(md_filename) as f:
                    content = f.read()
                self.assertGreater(
                    len(content), 0,
                    msg='MD file "%s" is empty' % (md_filename)
                )

    def test_md_files_are_not_containing_ad_blocks_prohibited_keywords(self):
        """Test that the MD files are not containing prohibited keywords."""
        books = Books()
        for book in books.books:
            self.assertFalse(
                'advertising' in book.md_paths,
                msg='MD file "%s" contains "advertising"' % (book.md_paths)
            )
