import unittest

from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(None), 'You didn\'t enter any text')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(None), 'Vous n\'avez entré aucun texte')

unittest.main()