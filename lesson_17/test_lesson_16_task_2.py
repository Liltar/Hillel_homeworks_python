from lesson_16 import task_2
import unittest


class PhoneNumberTest(unittest.TestCase):
    def test_formatting(self):
        self.assertEqual(task_2.format_phone_number('380639999999'), '(+38) 063 999-99-99')


if __name__ == '__main__':
    unittest.main()