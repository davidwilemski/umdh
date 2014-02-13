
import json
import umdh.umdh
import unittest


class SearchMenuForTests(unittest.TestCase):
    def test_search_menu(self):
        """
        Haven't yet figured out a good way of testing
        get_menu and get_menu_xml without other dependancies...

        So. This is the only test for now:
        """
        self.assertTrue(
            umdh.search_menu_for(
                self.menu,
                'Chocolate Chip Cookies'))  # assumes there's always cookies...

    def setUp(self):
        """
        Nasty setup function that stores what a real document looks like
        """
        url = umdh.umdh.dining_halls['marketplace']
        self.menu = umdh.get_menu(url)

if __name__ == '__main__':
    unittest.main()
