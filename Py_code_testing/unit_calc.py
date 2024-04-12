import unittest
import Unit_testing

class TestClac(unittest.TestCase): # inheriting from unittest module the Testcase class
     
     #defining the method , the method needs to start with test_ to know which methods reprents test
    def test_add(self):
        #result =Unit_testing.add(10,5)
        #self.assertEqual(result,14)
        self.assertEqual(Unit_testing.add(10,5),15)
          #checking the mulitple edge cases
        self.assertEqual(Unit_testing.add(-1,1),0) 
        self.assertEqual(Unit_testing.add(-1,-1),-2) 
        self.assertEqual(Unit_testing.add(0,0),0)   #ruuning only one test: test_add

    def test_subtract(self):
        self.assertEqual(Unit_testing.subtract(10,5),5)
        self.assertEqual(Unit_testing.subtract(-1,1),-2) 
        self.assertEqual(Unit_testing.subtract(-1,-1),0) 
     
    def test_multiply(self):
        self.assertEqual(Unit_testing.multiply(10,5),50)
        self.assertEqual(Unit_testing.multiply(-1,1),-1) 
        self.assertEqual(Unit_testing.multiply(-1,-1),1) 
 
    def test_divide(self):
        self.assertEqual(Unit_testing.divide(10,5),2)
        self.assertEqual(Unit_testing.divide(-1,1),-1) 
        self.assertEqual(Unit_testing.divide(-1,-1),1) 
        self.assertEqual(Unit_testing.divide(5,2),2.5)  
         #must add this case so that the case will give error if it is floor division
    
        self.assertRaises(ValueError, Unit_testing.divide,10 ,0) #to test the zero division error
    # Or using the context Manager for exceptions
        with self.assertRaises(ValueError):
            Unit_testing.divide(10,0)


# '..F.' here dot indicates that the test case is passed and F indicates that it is failed

#navigate module dir and in  cmd  run "pyhton -m unittest unit_calc.py"

# To run the method directly in cmmd and terminal 

if __name__ == '__main__':
    unittest.main()