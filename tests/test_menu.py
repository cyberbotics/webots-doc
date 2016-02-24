"""Test module of the menu.md files."""
import os
import re
import unittest


class TestMenu(unittest.TestCase):
    """Unit test of the menus."""

    def setUp(self):
        """Setup."""
        # path to the main project
        self.project_path = os.path.abspath(os.path.join(
            os.path.dirname(os.path.realpath(__file__)), os.pardir))
        # discover the menu.md files
        self.menus = []
        for item in os.listdir(self.project_path):
            path = os.path.join(self.project_path, item)
            if (os.path.isdir(path) and
                    not item.startswith('.') and
                    not item == 'tests'):
                self.menus.append(os.path.join(path, 'menu.md'))

    def test_menu_files_are_existing(self):
        """The menu.md files are existing in each book."""
        self.assertGreater(len(self.menus), 0, msg='No menu found')
        for menu in self.menus:
            self.assertTrue(
                os.path.isfile(menu),
                msg='File "%s" is not existing' % (menu)
            )

    def test_menu_are_refering_valid_files(self):
        """The menu.md references are pointing on valid files."""
        for menu in self.menus:
            with open(menu) as f:
                content = f.readlines()
            self.assertGreater(len(content), 0, msg='Menu file is empty')
            match_counter = 0
            for line_number in range(0, len(content)):
                line = content[line_number].strip()
                if len(line) == 0:
                    continue
                else:
                    match = re.match(r'^- \[(.*)\]\((.*)\)$', line)
                    self.assertIsNotNone(
                        match, msg='Line %d of "%s" does not match \
                        the expected pattern' % (line_number, menu)
                    )
                    for i in [1, 2]:
                        self.assertTrue(
                            match.group(i) and len(match.group(i)) > 0,
                            msg='Line %d of "%s" does not match' %
                            (line_number, menu)
                        )
                    match_counter += 1

                    target_file = os.path.join(
                        os.path.dirname(menu), match.group(2)
                    )
                    self.assertTrue(
                        os.path.isfile(target_file),
                        msg='' % ()
                    )
            self.assertGreater(
                match_counter, 0,
                msg='Menu "%s" do not contain valid references' % (menu)
            )

    def test_all_book_files_are_referred_by_the_menu_file(self):
        """All the book files are referred by the menu files."""
        for menu in self.menus:
            book_path = os.path.dirname(menu)
            book_name = os.path.basename(book_path)
            # list md files in bookPath
            with open(menu, 'r') as menu_file:
                menu_content = menu_file.read()
            for file_path in os.listdir(book_path):
                if (file_path.endswith(".md") and
                        file_path != (book_name + '.md') and
                        file_path != "menu.md"):
                    self.assertIn(
                        file_path, menu_content,
                        msg='"%s" not referenced in "%s"' %
                        (file_path, menu)
                    )
