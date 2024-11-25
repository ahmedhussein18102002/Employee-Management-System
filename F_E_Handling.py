# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:48:34 2024

@author: Ahmed Hussein
"""
# regular expression module
import re
import csv
import utils
def load_from_csv():
    with open(utils.file,mode='r') as data:
        read =csv.DictReader(data)
        for row in read:
            utils.employees_list[row['id']]={
                'name': row['name'],
                'position': row['position'],
                'salary': row['salary'],
                'email': row['email']
                }

def store_in_csv(data):
    fieldnames = ['id', 'name', 'position', 'salary', 'email']
    with open(utils.file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for emp_id in data:
            writer.writerow({
                'id': emp_id,
                'name': data[emp_id]['name'],
                'position': data[emp_id]['position'],
                'salary': data[emp_id]['salary'],
                'email': data[emp_id]['email']
            })

def check_email(email):
    # regular expression
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    flag = re.match(email_regex, email)
    if flag:
        return False
    else:
        print('wrong email!!!')
        return True
    