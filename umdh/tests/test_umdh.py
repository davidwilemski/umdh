
import datetime
import umdh
import unittest


class SearchMenuForTests(unittest.TestCase):
    def test_search_menu(self):
        """
        So. This is a dumb test.
        """
        self.assertTrue(
            umdh.search_menu_for(
                self.menu,
                'Chocolate Chip Cookies'))  # assumes there's always cookies...

    def test_get_menu_url(self):
        """
        test that we return correct URLs with and without a date passed
        """
        location = 'markley'

        url = umdh.get_menu_url(location)
        self.assertEqual(url, 'http://www.housing.umich.edu/files/helper_files/js/xml2print.php?location=MARKLEY%20DINING%20HALL&output=json&date=today')

        url = umdh.get_menu_url(location, datetime.date(2014, 3, 11))
        self.assertEqual(url, 'http://www.housing.umich.edu/files/helper_files/js/xml2print.php?location=MARKLEY%20DINING%20HALL&output=json&date=Tuesday,March 11')

    def setUp(self):
        """
        Nasty setup function that stores what a real document looks like
        """
        url = umdh.dining_halls['marketplace']
        self.menu = umdh.get_menu(url)

if __name__ == '__main__':
    unittest.main()
