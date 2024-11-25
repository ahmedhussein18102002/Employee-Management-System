# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:43:57 2024

@author: Ahmed Hussein
"""
from EManaging import EmpManage
import F_E_Handling as handler
import sys

def menu():
    print('--------------------------------------------')
    print('select operation from menu:')
    print('1.add new employee.')
    print('2.update employee data.')
    print('3.delete employee.')
    print('4.search for an employee.')
    print('5.list all employees.')
    print('6.exit')

def exitt():
    sys.exit(0)
    
handler.load_from_csv()
manager = EmpManage()

while True:
    menu()
    selection = input('_> ')
    menu_list = {'1': manager.add_employee,
                 '2': manager.update_employee,
                 '3': manager.delete_employee,
                 '4': manager.search_employee,
                 '5': manager.list_employees,
                 '6': exitt
                 }
    menu_list[selection]()
 

