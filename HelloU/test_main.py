import unittest
import main

class TestMain(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = main.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = main.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main':
    unittest.main()
