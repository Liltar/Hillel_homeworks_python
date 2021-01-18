import unittest
from lesson_7 import task_2


class ConverterTest(unittest.TestCase):

    def test_celsius(self):
        self.assertEqual(task_2.celsius(), 32, 273)

if __name__ == '__main__':
    unittest.main()