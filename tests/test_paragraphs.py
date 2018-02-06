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

    def test_one_sentence_per_line(self):
        """Test that each sentence is written on one line."""
        for p in self.paragraphs:
            lines = p.split('\n')
            for line in lines:
                if len(line.strip()) == 0:
                    continue
                if '**Keywords**' in line:
                    continue
                self.assertTrue(line.endswith('.') or line.endswith(':'), msg='The following line does not end with a period: "%s"' % line)
