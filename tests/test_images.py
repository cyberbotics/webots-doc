"""Test module of the images."""
import unittest
from books import Books

import os
import re


class TestImages(unittest.TestCase):
    """Unit test of the images."""

    def test_images_are_valid(self):
        """Test that the MD files are pointing on valid URLs."""
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                with open(md_path) as f:
                    content = f.read()
                for match in re.finditer(r"!\[(.*?)\]\((.*?)\)", content):
                    # remove parameters
                    image_ref = match.group(2).split(' ')[0]
                    image_path = os.path.join(book.path, image_ref)
                    self.assertTrue(
                        os.path.isfile(image_path),
                        msg='%s: "%s" not found' % (md_path, image_path)
                    )
