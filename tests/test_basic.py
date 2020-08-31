
import pdfmerger
import unittest


class BasicTestCase(unittest.TestCase):
    """ Basic test cases """

    def test_basic(self):
        """ check True is True """
        self.assertTrue(True)

    def test_version(self):
        """ check pdfmerger exposes a version attribute """
        self.assertTrue(hasattr(pdfmerger, "__version__"))
        self.assertIsInstance(pdfmerger.__version__, str)


if __name__ == "__main__":
    unittest.main()
