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
                # Extract MD content.
                with open(md_path) as f:
                    content = f.read()

                # Remove annoying string sequences.
                # - Headers.
                content = re.sub(r'^#.*', '', content)
                content = re.sub(r'\n#.*', '\n', content)
                # - Multiline code sections.
                content = re.sub(r'```.*```', '', content, flags=re.S)
                # - Items.
                content = re.sub(r'\n\s*-.*', '', content)
                content = re.sub(r'\n\s*\d+\..*', '', content)
                # - Showdown extensions.
                content = re.sub(r'%figure.*%end', '', content, flags=re.S)
                content = re.sub(r'%api.*%end', '', content, flags=re.S)

                # Extract paragraphs (and notes)
                for match in re.finditer(r'(?s)((?:[^\n][\n]?)+)', content):
                    paragraph = content[match.start():match.end() - 1]
                    # - Arrays.
                    if paragraph.startswith('| '):
                        continue
                    self.paragraphs.append(paragraph)
        # Debug: Uncomment to display all the acquired paragraphs.
        # for p in self.paragraphs:
        #     print ('@@@')
        #     print (p)

    def test_something(self):
        """TODO."""
        pass
