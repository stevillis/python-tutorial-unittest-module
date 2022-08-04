"""Test module for Employee class"""
import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test Employee methods"""

    @classmethod
    def setUpClass(cls):  # runs once, before first setUp
        print('setUpClass')
        cls.emp_1 = Employee('Sara', 'Kerkhoff', 5000)
        cls.emp_2 = Employee('Sam', 'Martin', 4500)
        cls.emp_3 = Employee('Joe', 'Kenedy', 5500)

    @classmethod
    def tearDownClass(cls):  # runs once, after last tearDown
        print('tearDownClass')

    def setUp(self):  # runs before each test
        print('setUp')

    def tearDown(self):  # runs after each test
        print('tearDown')

    def test_email(self):
        """Test employee email property"""
        print('test_email')
        self.assertEqual(self.emp_1.email, 'sara.kerkhoff@email.com')

        with self.subTest('Change Employee first name'):
            self.emp_2.first_name = 'Zack'
            self.assertEqual(self.emp_2.email, 'zack.martin@email.com')

        with self.subTest('Change Employee last name'):
            self.emp_3.last_name = 'Obama'
            self.assertEqual(self.emp_3.email, 'joe.obama@email.com')

    def test_fullname(self):
        """Test employee fullname property"""
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Sara Kerkhoff')

        with self.subTest('Change Employee first name'):
            self.emp_2.first_name = 'Zack'
            self.assertEqual(self.emp_2.fullname, 'Zack Martin')

        with self.subTest('Change Employee last name'):
            self.emp_3.last_name = 'Obama'
            self.assertEqual(self.emp_3.fullname, 'Joe Obama')

    def test_pay(self):
        """Test employee pay method"""
        print('test_pay')
        self.assertEqual(self.emp_1.pay, 5000)

        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 5250)


if __name__ == '__main__':
    unittest.main()
