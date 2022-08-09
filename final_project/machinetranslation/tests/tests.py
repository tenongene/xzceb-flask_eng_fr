import unittest
from translator import englishToFrench, frenchToEnglish

class TranslationTestCase(unittest.TestCase):
    
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        
    def test_nullToFrench(self):
        self.assertRaises(TypeError, englishToFrench,)
        
    def test_nullToEnglish(self):
        self.assertRaises(TypeError, frenchToEnglish,)
        
    def test_noneToFrench(self):
        self.assertRaises(ValueError, englishToFrench, None)
        
    def test_noneToEnglish(self):
        self.assertRaises(ValueError, frenchToEnglish, None)
        
        
if __name__ == '__main__':
    unittest.main()