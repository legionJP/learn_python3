import unittest
from employee import Employee
from unittest.mock import patch
import employee
class TestEmployee(unittest.TestCase):

    #setUP and #tearDown method for avoidinng the repetation in code

    #for class method refer to 'test_Employee2.py'

    def setUp(self):
        self.emp_1 = Employee('Abba','Sabba',50000)
        self.emp_2 = Employee('Hamba','Kamba',60000) 
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
    
    #Note: In a setUp method you could create the test directory or the test database to hold those 
    #file , 2. In a teraDown Method you could delete all of those so you could have clean slate for next test.


    def test_email(self):
        # emp_1 = Employee('Abba','Sabba',50000)
        # emp_2 = Employee('Hamba','Kamba',60000)
        
        self.assertEqual(self.emp_1.email,'Abba.Sabba@email.com')
        self.assertEqual(self.emp_2.email,'Hamba.Kamba@email.com')

        self.emp_1.first = 'Dabba'
        self.emp_2.first = 'Damba'

        self.assertEqual(self.emp_1.email,'Dabba.Sabba@email.com')
        self.assertEqual(self.emp_2.email,'Damba.Kamba@email.com')

    def test_fullname(self):
        # emp_1 = Employee('Abba','Sabba',50000)
        # emp_2 = Employee('Hamba','Kamba',60000)

        self.assertEqual(self.emp_1.fullname,'Abba Sabba')
        self.assertEqual(self.emp_2.fullname,'Hamba Kamba')
        
        self.emp_1.first = 'Dabba'
        self.emp_2.first = 'Damba'

        self.assertEqual(self.emp_1.fullname,'Dabba Sabba')
        self.assertEqual(self.emp_2.fullname,'Damba Kamba')

    def test_apply_raise(self):

        # emp_1 = Employee('Abba','Sabba',50000)
        # emp_2 = Employee('Hamba','Kamba',60000)
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay,63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get: 
            #Using the context manager and we want to mock requests.get , the object of employee
            mocked_get.return_value.ok = True
            mocked_get.return_value.text= 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Abba/May')
            self.assertEqual(schedule,'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Hamba/June')
            self.assertEqual(schedule,'Bad Response!')


        
if __name__ =='__main__':
    unittest.main()
 


#Note : The tests should be isolated means your test should not be rely on the other test or affect the 
# other test 
# Test Driven Development : Write the test before the code , means Think about your code that what you 
#want to do and than write the test to implement behaviour and test fails then fix this 






