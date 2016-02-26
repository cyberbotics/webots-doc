"""Test module of the references."""
import unittest
from books import Books

from email.utils import parseaddr
import os
import re


def slugify(txt):
    """Slugify function."""
    output = txt.lower()
    output = re.sub(r'<[^>]+>', '', output)
    output = output.replace('+', 'p')
    output = re.sub(r'[\(\):`]', '', output)
    output = re.sub(r'\W+', '-', output)
    output = re.sub(r'^-*', '', output)
    output = re.sub(r'-*$', '', output)
    return output.strip(' ').strip('-')


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
                    # 1. external link
                    if ref.startswith('www') or ref.startswith('http'):
                        continue
                    # 2. mailto
                    if ref.startswith('mailto:'):
                        mailto = ref[len('mailto:') + 1:]
                        (name, address) = parseaddr(mailto)
                        self.assertGreater(
                            address, 0,
                            msg='Invalid address "%s"' % (mailto)
                        )
                        continue
                    # 3. link to another MD file
                    ref = ref.split('#')
                    link = ref[0]
                    self.assertGreater(len(ref), 0, msg='Invalid reference')
                    self.assertTrue(
                        link.endswith('.md'),
                        msg='Invalid reference "%s" in %s:\n-> "%s"' %
                            (ref, md_path, m.group(0))
                    )
                    file_path = os.path.join(book.path, link)
                    self.assertTrue(
                        os.path.isfile(file_path),
                        msg='%s: "%s" not found' % (md_path, file_path)
                    )
                    # 4. Anchor
                    if len(ref) > 1:
                        anchor = ref[1]
                        with open(file_path) as f:
                            found = False
                            for line in f:
                                if anchor in line:
                                    found = True
                                    continue
                                elif line.startswith('#'):
                                    title = re.sub(r'^#*', '', line)
                                    if anchor == slugify(title):
                                        found = True
                                        continue
                                elif line.startswith('%figure'):
                                    title = line.replace('%figure', '')
                                    if anchor == slugify(title):
                                        found = True
                                        continue
                                elif line.startswith('%api'):
                                    title = line.replace('%api', '')
                                    if anchor == slugify(title):
                                        found = True
                                        continue
                        self.assertTrue(
                            found, msg='%s -> %s:%s not found' %
                            (md_path, file_path, anchor)
                        )
