"""Test module for the paragraphs."""

import unittest
import re

from books import Books


class TestParagraphs(unittest.TestCase):
    """Unit test of the paragraphs."""
    hyperlinkRE = re.compile(r'[^\!]\[([^\]]*)\]\s*\(([^\)]*)\)')

    def setUp(self):
        """Setup: get all the paragraphs and notes."""
        self.paragraphs = []
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                # Extract MD content.
                with open(md_path) as f:
                    content = f.read()

                # Remove annoying string sequences.
                # - Headers.
                content = re.sub(r'^#.*', '', content)
                content = re.sub(r'\n#.*', '\n', content)
                # - Multiline code sections.
                content = re.sub(r'```.+?(?=```)```', '', content, flags=re.S)
                # - Items.
                content = re.sub(r'\n\s*-.*', '', content)
                content = re.sub(r'\n\s*\d+\..*', '', content)
                # - Showdown extensions.
                content = re.sub(r'%figure.+?(?=%end)%end', '', content, flags=re.S)
                content = re.sub(r'%api.+?(?=%end)%end', '', content, flags=re.S)

                # Extract paragraphs and notes.
                for match in re.finditer(r'(?s)((?:[^\n][\n]?)+)', content):
                    paragraph = content[match.start():match.end() - 1]
                    # - Arrays.
                    if paragraph.startswith('| '):
                        continue
                    self.paragraphs.append(paragraph)
        # Debug: Uncomment to display all the acquired paragraphs and notes.
        # for p in self.paragraphs:
        #     print ('@@@')
        #     print (p)

    def test_code_inside_hyperlink_is_forbidden(self):
        """Test that no code is inserted inside hyperlinks."""
        for p in self.paragraphs:
            for m in re.finditer(self.hyperlinkRE, p):
                linkName = m.group(1).strip()
                self.assertFalse('`' in linkName, msg='Hyperlink "%s" contains code.' % m.group(0))

    def test_underscores_in_hyperlinks_are_protected(self):
        """Test that every underscores appearing in hyperlinks are protected."""
        for p in self.paragraphs:
            for m in re.finditer(self.hyperlinkRE, p):
                linkName = m.group(1).strip()
                self.assertTrue(re.search(r'[^\\]_', linkName) is None, msg='Hyperlink "%s" contains unprotected underscore(s).' % m.group(0))

    def test_hyperlinks_do_not_contain_prohibited_characters(self):
        """Test that hyperlinks are not containing prohibited characters (such as '<')."""
        for p in self.paragraphs:
            for m in re.finditer(self.hyperlinkRE, p):
                linkName = m.group(1).strip()
                self.assertTrue(re.search(r'[<>]', linkName) is None, msg='Hyperlink "%s" contains forbidden characters.' % m.group(0))
