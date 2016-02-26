"""Test module of the MD files."""
import unittest
import os
from books import Books


class TestMDFiles(unittest.TestCase):
    """Unit test of the MD files."""

    def setUp(self):
        """Setup."""
        pass

    def test_md_files_are_existing(self):
        """Test that the MD files are existing."""
        books = Books()
        self.assertGreater(len(books.books), 0, msg='No books found')
        for book in books.books:
            md_filenames = books.get_md_files(book)
            self.assertGreater(
                len(md_filenames), 0,
                msg='No MD files found in book "%s"' % book
            )
            for md_filename in md_filenames:
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
