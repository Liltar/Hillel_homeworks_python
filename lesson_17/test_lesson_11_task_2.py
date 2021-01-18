from lesson_11 import task_2
import unittest

class TestHideNameFunc(unittest.TestCase):
    def test_hide_name(self):
        self.assertEqual(task_2.hide_email('somebody_email@gmail.com'), 'somebody_em***@**ail.com')

if __name__ == '__main__':
    unittest.main()