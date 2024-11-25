# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:47:33 2024

@author: Ahmed Hussein
"""

class EmployeeClass :
    def __init__(self):
        self.employee = {
            'name': '',
            'position': '',
            'salary': 0,
            'email': ''
        }
    def new_employee(self,id,name,position,salary,email):
        self.employee['name']=name
        self.employee['position']=position
        self.employee['salary']=salary
        self.employee['email']=email
        return self.employee
        
        