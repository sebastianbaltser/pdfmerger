"""
    Tests for pdfmerger.
"""
import unittest

import src.pdfmerger.pdfmerger as pdfmerger


class StripTitleTest(unittest.TestCase):
    """ Basic test cases """

    def test_basic(self):
        """ check that the function works for a basic case """
        result = pdfmerger.strip_title("Interesting title (123) [321]")
        self.assertEqual("Interesting title", result)

if __name__ == "__main__":
    unittest.main()
