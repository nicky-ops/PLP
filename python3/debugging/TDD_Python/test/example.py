import unittest

def add(a, b):
    return a + b
class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(10, 20)
        self.assertEqual(result, 30)

if __name__ == '__main__':
    unittest.main()
