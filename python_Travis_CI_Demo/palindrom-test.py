import unittest
from palindromCheck import palindromCheck
# import palindromeCheck

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(palindromCheck('abc'), 0)
       # self.assertEqual(palindromCheck('aba'), 1)
       # self.assertEqual(palindromCheck('123'), 0)
       # self.assertEqual(palindromCheck('121'), 1)
        
if __name__ == '__main__':
    unittest.main()
