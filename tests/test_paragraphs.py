"""Test module for the paragraphs."""

import unittest
import re

from books import Books


class TestParagraphs(unittest.TestCase):
    """Unit test of the paragraphs."""

    hyperlinkRE = re.compile(r'[^\!]\[([^\]]*)\]\s*\(([^\)]*)\)')

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
                # - Multiline code sections.
                content = re.sub(r'```.+?(?=```)```', '\n', content, flags=re.S)
                content = re.sub(r'\n`.+?(?=`\n)`\n', '\n', content, flags=re.S)
                # - Notes.
                content = re.sub(r'\n\s*>.+?(?=\n\n)', '\n', content, flags=re.S)
                content = re.sub(r'\n\s*>.+?(?=\n$)', '\n', content, flags=re.S)
                # - Showdown extensions.
                content = re.sub(r'%figure.+?(?=%end)%end', '\n', content, flags=re.S)
                content = re.sub(r'%api.+?(?=%end)%end', '\n', content, flags=re.S)
                # - Headers.
                content = re.sub(r'^#.*', '\n', content)
                content = re.sub(r'\n#.*', '\n', content)
                # - Items.
                content = re.sub(r'\n\s*-.+?(?=\n\n)', '\n', content, flags=re.S)
                content = re.sub(r'\n\s*-.+?(?=\n$)', '\n', content, flags=re.S)
                content = re.sub(r'\n\s*\d+\..+?(?=\n\n)', '\n', content, flags=re.S)
                content = re.sub(r'\n\s*\d+\..+?(?=\n$)', '\n', content, flags=re.S)
                content = re.sub(r'\n    .+?(?=\n)', '\n', content, flags=re.S)
                content = re.sub(r'\n        .+?(?=\n)', '\n', content, flags=re.S)
                # - HTML statements
                content = re.sub(r'\n<.+?>\n', '\n', content, flags=re.S)
                content = re.sub(r'\n---\n', '\n', content, flags=re.S)
                # - Single hyperlinks
                content = re.sub(r'\n\!?\[.+\)\n', '\n', content, flags=re.S)
                # - Special statements
                content = re.sub(r'\nRelease {{.+?}}\n', '\n', content, flags=re.S)
                content = re.sub(r'\n\s*\*\*.+?\n', '\n', content, flags=re.S)
                content = re.sub(r'\n\s*\*.+?\*\n', '\n', content, flags=re.S)
                content = re.sub(r'\n\s*\{.+?\n', '\n', content, flags=re.S)

                # Extract paragraphs.
                for match in re.finditer(r'(?s)((?:[^\n][\n]?)+)', content):
                    paragraph = content[match.start():match.end() - 1]
                    # - Arrays.
                    if paragraph.startswith('| ') or paragraph.startswith('> '):
                        continue
                    self.paragraphs.append({'paragraph': paragraph, 'md': md_path})
        # Debug: Uncomment to display all the acquired paragraphs.
        # for p in self.paragraphs:
        #     print ('@@@')
        #     print (p)

    def test_one_sentence_per_line(self):
        """Test that each sentence is written on one line."""
        for p in self.paragraphs:
            lines = p['paragraph'].split('\n')
            for line in lines:
                if len(line.strip()) == 0:
                    continue
                if '**Keywords**' in line:
                    continue
                self.assertTrue(
                    line.endswith('.') or line.endswith(':') or line.endswith('!'),
                    msg='%s: The following line does not end correctly: "%s"' % (p['md'], line)
                )
