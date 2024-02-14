import unittest

class TestStringMethod(unittest.TestCase):

   def test_strUpper(self):
      str_new = "ABC"
      self.assertTrue(str_new.isupper)

if __name__ == '__main__': 
    unittest.main()       