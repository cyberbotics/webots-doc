"""Test module for the hyperlinks."""

import unittest
import re

from books import Books


class TestHyperlinks(unittest.TestCase):
    """Unit test of the hyperlinks."""

    def setUp(self):
        """Setup: get all the hyperlinks."""
        self.hyperlinks = []

        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                # Extract MD content.
                with open(md_path) as f:
                    content = f.read()
                # Remove code statements
                content = re.sub(r'```.+?(?=```)```', '', content, flags=re.S)
                content = re.sub(r'`.+?(?=`)`', '', content, flags=re.S)
                # Extract hyperlinks.
                for m in re.finditer(r'[^\!](\[([^\]]*)\]\s*\(([^\)]*)\))', content):
                    hyperlinkMD = m.group(1)
                    hyperlinkName = m.group(2)
                    hyperlinkUrl = m.group(3)
                    self.hyperlinks.append({
                        'md': hyperlinkMD,
                        'name': hyperlinkName,
                        'url': hyperlinkUrl,
                        'file': md_path
                    })
        # # Debug: Uncomment to display all the acquired hyperlinks.
        # for h in self.hyperlinks:
        #     print (h)

    def test_underscores_in_hyperlinks_are_protected(self):
        """Test that every underscores appearing in hyperlinks are protected."""
        for h in self.hyperlinks:
            self.assertTrue(
                re.search(r'[^\\]_', h['name']) is None,
                msg='Hyperlink "%s" contains unprotected underscore(s) in "%s".' % (h['md'], h['file'])
            )

    def test_hyperlinks_do_not_contain_prohibited_characters(self):
        """Test that hyperlinks are not containing prohibited characters (such as '<')."""
        for h in self.hyperlinks:
            self.assertTrue(
                re.search(r'[<>]', h['name']) is None,
                msg='Hyperlink "%s" contains forbidden characters in "%s".' % (h['md'], h['file'])
            )
