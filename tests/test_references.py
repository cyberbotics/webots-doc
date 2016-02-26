"""Test module of the references."""
import unittest
from books import Books

from email.utils import parseaddr
import os
import re


class TestReferences(unittest.TestCase):
    """Unit test of the references."""

    def test_references_are_valid(self):
        """Test that the MD files are pointing on valid URLs."""
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                with open(md_path) as f:
                    content = f.read()
                for m in re.finditer(r"[^!]\[(.*?)\]\(([^\)]+)\)", content):
                    # remove parameters
                    ref = m.group(2)
                    if ref.startswith('www') or ref.startswith('http'):
                        continue
                    if ref.startswith('mailto:'):
                        mailto = ref[len('mailto:') + 1:]
                        (name, address) = parseaddr(mailto)
                        self.assertGreater(
                            address, 0,
                            msg='Invalid address "%s"' % (mailto)
                        )
                        continue
                    ref = ref.split('#')
                    self.assertGreater(len(ref), 0, msg='Invalid reference')
                    self.assertTrue(
                        ref[0].endswith('.md'),
                        msg='Invalid reference "%s" in %s:\n-> "%s"' %
                            (ref, md_path, m.group(0))
                    )
                    file_path = os.path.join(book.path, ref[0])
                    self.assertTrue(
                        os.path.isfile(file_path),
                        msg='%s: "%s" not found' % (md_path, file_path)
                    )
