# Review Programming Assignment
# Program Description:
# Your Name: Victor Soto
# Date: 9/22/2026



# Employee Class
import re


class Employee:
    """ Employee class to keep track employee info """
    # initializer
    def __init__(self, ID=-999, name='', department='', pay=0.0):
        """ initializer for new employee object """
        self.set_ID(ID)
        self.set_name(name)
        self.set_department(department)
        self.set_pay(pay)
    # getters and setters
    def get_ID(self):
        return self.ID
        
    def set_ID(self,ID):
        self.ID = ID
        
    def get_name(self):
        return self.name
        
    def set_name(self,name):
        self.name = name
    def get_department(self):
        return self.department
    def set_department(self, department):
        self.department = department
    def get_pay(self):
        return self.pay

    def set_pay(self, pay):
        self.pay = pay
    # methods
    
    def __str__(self):
        """ return employee object in string """
        return f'{self.get_ID()}\t{self.get_name()}\t{self.get_department()}\t{self.get_pay()}'



class EmployeeDirectory:
    #""" Track employee info in the directory """
    def __init__(self):
        #""" initialize employee_list and employee_dict """
        self.employee_list = []
        self.employee_dict = {}

        
    def add_employee(self, employee):
        """ append employee object to the employee_list """
        # check for duplicates
        if employee not in self.employee_list:
            self.employee_list.append(employee)
    
    def del_employee(self, employee):
        """ delete employee object from the employee_list """
        # check for duplicates
        if employee in self.employee_list:
            self.employee_list.remove(employee)
        else:
            return f'ID {employee.get_ID()} does not exist. deletion is aborted'
    
    def read_file(self,file_name):
        """ read employeex.txt file and store the data into a list of employee objects and return it """
         
        with open(file_name, 'r') as file:
            employees = []
            for line in file:
                
                split_line = line.strip().split(' ')
                add_to_list = Employee(int(split_line[0]), split_line[1], split_line[2], float(split_line[3]))
                employees.append(add_to_list)
        return employees
        

    def update_employee_dir(self,file_name):
        """ call read_file and update the employee_list attribute """
        self.employee_list = self.read_file(file_name)
        
    def write_to_file(self,file_name):
        """ write the updated employee_list to file """
        with open(file_name, 'w') as file:
            for emp in self.employee_list:
                file.write(f'{emp.get_ID()} {emp.get_name()} {emp.get_department()} {emp.get_pay()}\n')

                
    def write_to_dict(self):
        """ write employee_list data to a dictionary of lists, update the employee_dict attribute """

        
        # create a dummy employee object
        dummy_emp = Employee()
        for attribute_name, attribute_value in dummy_emp.__dict__.items():
            self.employee_dict[attribute_name]=[]

        for emp in self.employee_list:
            # each attribute in the object is stored in obj.__dict__
            for attribute_name, attribute_value in emp.__dict__.items():
                self.employee_dict[attribute_name].append(attribute_value)
        

        self.employee_dict = {'ID': [], 'name': [], 'department': [], 'pay': []}
        for emp in self.employee_list:
            self.employee_dict['ID'].append(emp.get_ID())
            self.employee_dict['name'].append(emp.get_name())
            self.employee_dict['department'].append(emp.get_department())
            self.employee_dict['pay'].append(emp.get_pay())
            
    def display_dict(self):
        """ display employee dictionary in key/value pairs """
           
        for key, value in self.employee_dict.items():
           print(f'{key}: {value}')


        
# test class
if __name__ == '__main__':

    try:
        # Create an object of EmployeeDirectory - complete the code here
        emp_dir = EmployeeDirectory()
        
        # Call update_employee_dir() method - complete the code here
        emp_dir.update_employee_dir('employees.txt')

        # Add 3 employee objects here - see assignment instructions - complete the code here
        emp1 = Employee(106, 'Emp1', 'Accounting', 56000.0)
        emp2 = Employee(107, 'Emp2', 'Sales', 80000.0)
        emp3 = Employee(108, 'Emp3', 'Marketing', 90000.0)

        # Call add_employee() method Add emp1 and emp2 objects - complete the code here
        emp_dir.add_employee(emp1)
        emp_dir.add_employee(emp2)

        # Call del_employee() method to delete emp3 objects - complete the code here
        del_emp = Employee(108, 'Emp3', 'Marketing', 90000.0)
        result = emp_dir.del_employee(del_emp)
        print(result)
        # call write_to_file() method to overwrite the txt file employees.txt
        emp_dir.write_to_file('employees.txt')
        # call write_to_dict() method to create a dictionary
        emp_dir.write_to_dict()
        # call display_dict() to display the output
        emp_dir.display_dict()        

    except FileNotFoundError as fnfe:
        print(fnfe)
    except KeyError as ke:
        print(ke)
    except Exception as ex:
        print(ex)        
                      
    finally:
        print(f'Program is completed')
        
                               
                               
                         
