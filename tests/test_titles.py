"""Test module for the titles."""

import unittest
import re

from books import Books


class TestTitles(unittest.TestCase):
    """Unit test of the titles."""

    def setUp(self):
        """Setup: get all the titles."""
        self.titles = []
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                # Extract MD content.
                with open(md_path) as f:
                    content = f.read()

                # Remove annoying string sequences.
                # - Multiline code sections.
                content = re.sub(r'```.+?(?=```)```', '', content, flags=re.S)

                # Extract titles.
                for match in re.finditer(r'#+ .*', content):
                    title = content[match.start():match.end()]
                    self.titles.append({'title': title, 'md': md_path})
        # Debug: Uncomment to display all the acquired titles.
        # for t in self.titles:
        #     print (t)

    def test_underscores_are_protected(self):
        """Test that titles doesn't contain any unprotected underscore."""
        for t in self.titles:
            self.assertTrue(re.search(r'[^\\]_', t['title']) is None, msg='%s: Title "%s" contains unprotected underscore(s).' % (t['md'], t['title']))

    def test_words_are_capitalized(self):
        """Test that title words are capitalized."""
        # Rules reference: http://grammar.yourdictionary.com/capitalization/rules-for-capitalization-in-titles.html
        uppercasePattern = re.compile("^[A-Z][^A-Z]*$")
        lowercasePattern = re.compile("^[a-z][^A-Z]*$")
        for t in self.titles:
            title = re.sub(r'^#+\s*', '', t['title'])  # Remove the '#'+ suffix.
            title = re.sub(r'".+?(?=")"', '', title)  # Remove double-quoted statements.
            words = title.split()
            for w in range(len(words)):
                word = words[w]
                if word.startswith('wb_') or word.endswith('.wbt'):
                    continue
                if w == 0:
                    self.assertTrue(uppercasePattern.match(word), msg='%s: First word of title "%s" is not an uppercase.' % (t['md'], t['title']))
                elif w == len(words) - 1:
                    self.assertTrue(uppercasePattern.match(word), msg='%s: Last word of title "%s" is not an uppercase.' % (t['md'], t['title']))
                elif word.lower() in ['a', 'an', 'and', 'in', 'or', 'the']:
                    self.assertTrue(lowercasePattern.match(word), msg='%s: word "%s" of title "%s" is not an uppercase.' % (t['md'], word, t['title']))
                else:
                    self.assertTrue(uppercasePattern.match(word), msg='%s: word "%s" of title "%s" is not an lowercase.' % (t['md'], word, t['title']))
