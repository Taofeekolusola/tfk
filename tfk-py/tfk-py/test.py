import unittest
x = 5
y = x
class simple_test(unittest.TestCase):
    def test_isDigit(self):
        self.assertTrue('12' .isdigit())
    def test_isgreater(self):
        self.assertTrue(3>2)
    def test_xIsy(self):
        self.assertIs('x', 'x')

if __name__ == '__main__':
        unittest.main()
