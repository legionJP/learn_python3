import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    #setUP and #tearDown method for avoidinng the repetation in code

    def setUp(self):
        self.emp_1 = Employee('Abba','Sabba',50000)
        self.emp_2 = Employee('Hamba','Kamba',60000) 
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

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
        emp_1 = Employee('Abba','Sabba',50000)
        emp_2 = Employee('Hamba','Kamba',60000)

        self.assertEqual(emp_1.fullname,'Abba Sabba')
        self.assertEqual(emp_2.fullname,'Hamba Kamba')
        
        emp_1.first = 'Dabba'
        emp_2.first = 'Damba'

        self.assertEqual(emp_1.fullname,'Dabba Sabba')
        self.assertEqual(emp_2.fullname,'Damba Kamba')

    def test_apply_raise(self):

        emp_1 = Employee('Abba','Sabba',50000)
        emp_2 = Employee('Hamba','Kamba',60000)
        
        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay,63000)
        
if __name__ =='__main__':
    unittest.main()
 








