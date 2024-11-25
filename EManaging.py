# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:52:05 2024

@author: Ahmed Hussein
"""

from Employee import EmployeeClass
from tabulate import tabulate
import F_E_Handling as handler
import random
import utils
class EmpManage(): 
#--------------------    ADD NEW EMPLOYEE FUNCTION        ----------------------
    def add_employee(self):
        T=True
        while T:
            id=random.randint(1, 100000)
            #id = 94456
            if str(id) in utils.employees_list:
               T=True 
            else:
                T=False
        print('Enter employee data')
        name = input('name: ')
        position = input('position: ')
        salary = input('salary: ')
        self.x=True
        while (self.x) :
            email = input('email: ')
            self.x = handler.check_email(email)
        emp = EmployeeClass()
        utils.employees_list[id]=emp.new_employee(id, name, position, salary, email)
        handler.store_in_csv(utils.employees_list)
#--------------------    LIST EMPLOYEES DATA FUNCTION     ----------------------
    def list_employees(self):
        headers = ["ID", "Name", "Position", "Salary", "Email"]
        rows = [[id, utils.employees_list[id]['name'], utils.employees_list[id]['position'], utils.employees_list[id]['salary'], utils.employees_list[id]['email']] for id in utils.employees_list ]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
#--------------------    UPDATE EMPLOYEE DATA FUNCTION    ----------------------
    def update_employee(self):
        id = input('Enter employee id: ')
        flag = 0
        if id in utils.employees_list:
            headers = ["ID", "Name", "Position", "Salary", "Email"]
            row = [[id,utils.employees_list[id]['name'], utils.employees_list[id]['position'], utils.employees_list[id]['salary'], utils.employees_list[id]['email']]]
            print(tabulate(row, headers=headers, tablefmt="grid"))
            flag = True
            while flag:
                print('What would u want to change?')
                print('1.position')
                print('2.salary')
                print('3.email')
                selection =int( input('_> '))
                if selection == 1:
                    position = input('New position _> ')
                    utils.employees_list[id]['position'] = position
                elif selection == 2:
                    salary = input('New salary _> ')
                    utils.employees_list[id]['salary'] = salary
                elif selection == 3:
                     email = input('New email _> ')
                     utils.employees_list[id]['email'] = email
                       
                action = input('do u want to continue editing? 1.yes  2.No _> ')
                if int(action) == 2:
                    flag = False
                    print('employee data updated successfully!')
                    handler.store_in_csv(utils.employees_list)

#--------------------    DELETE EMPLOYEE FUNCTION         ----------------------
    def delete_employee(self):
        id = input('Enter employee id to delete : ')
        action = input('Are u sure? 1.yes  2.No _> ')
        if int(action) == 1:
            del utils.employees_list[id]
            print('employee data deleted successfully!')
            handler.store_in_csv(utils.employees_list)
     
#--------------------   SEARCH FOR EMPLOYEE FUNCTION      ----------------------
    def search_employee(self):
        i = input('Enter employee id: ')
        headers = ["ID", "Name", "Position", "Salary", "Email"]
        for id in utils.employees_list:
            if str(id) == str(i):
                row = [[id,utils.employees_list[id]['name'], utils.employees_list[id]['position'], utils.employees_list[id]['salary'], utils.employees_list[id]['email']]]
                print(tabulate(row, headers=headers, tablefmt="grid"))
                return  
        print('Employee not found')

