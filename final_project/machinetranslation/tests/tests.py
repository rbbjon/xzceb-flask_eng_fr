"""
    Purpose: run test translator check
"""
import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """
        Args:
        unittest (TestCase): Test Case translator
    """

    def test_english_to_french(self):
        """Translate english to french"""
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertNotEqual(english_to_french(''), '')

    def test_french_to_english(self):
        """
        Purpose: translate french to english
        """
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertNotEqual(french_to_english(''), '')

    # end def
