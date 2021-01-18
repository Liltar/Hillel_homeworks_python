import unittest
from lesson_7 import task_2


class ConverterTest(unittest.TestCase):

    def test_temp_calc(self):
        self.assertEqual(task_2.temp_calc(), 32)

if __name__ == '__main__':
    unittest.main()