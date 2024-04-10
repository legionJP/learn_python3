import unittest
import Unit_testing

class TestClac(unittest.TestCase): # inheriting from unittest module the Testcase class
     
     #defining the method , the method needs to staart with test_ to know which methods reprents test
    def test_add(self):
        result =Unit_testing.add(10,5)
        self.assertEqual(result,15) 

#navigate module dir and in  cmd  run "pyhton -m unittest unit_calc.py"

# To run the method directly in cmmd and terminal 

if __name__ == '__main__':
    unittest.main()