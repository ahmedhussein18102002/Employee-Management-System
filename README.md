
# Employee Management System

This Python-based **Employee Management System** provides functionalities to manage employee data efficiently. It allows users to add, update, delete, search, and list employee records. The system stores the employee data in a CSV file for persistent storage.

## Features
1. **Add New Employee**: Add new employee details including ID, name, position, salary, and email.
2. **Update Employee Data**: Modify the position, salary, or email of an existing employee.
3. **Delete Employee**: Remove an employee from the records.
4. **Search Employee**: Search for an employee by their unique ID.
5. **List Employees**: Display all employees in a tabular format.
6. **Persistent Data Storage**: Data is stored and retrieved from a CSV file.

---

## File Structure

### Main File
The entry point of the application that provides a menu-driven interface for the user to perform various operations.

### `EManaging` File
Defines the `EmpManage` class, which contains methods for:
- Adding, updating, and deleting employees.
- Listing employees in a tabular format.
- Searching for employees by ID.

### `F_E_Handling` File
Handles file operations:
- Loading employee data from the CSV file.
- Storing updated employee data into the CSV file.
- Validating email addresses with a regex.

### `Employee` File
Contains the `EmployeeClass`, which is responsible for creating a structured employee record.

### `utils` File
Holds global variables and configurations:
- `file`: The name of the CSV file where data is stored.
- `employees_list`: A dictionary to hold employee data in memory.

### `data.csv`
A CSV file where all employee records are stored. The columns include:
- `id`, `name`, `position`, `salary`, and `email`.

---

## Prerequisites

- Python 3.x
- Required libraries:
  - `tabulate`: To display data in a tabular format.
  - `csv`: To handle CSV file operations.
  - `re`: For email validation.

Install the required libraries using:
```bash
pip install tabulate
```

---

## How to Run

1. Clone the repository and navigate to the project directory.
2. Ensure the `data.csv` file exists in the same directory as the code files.
3. Run the main script:
   ```bash
   python main.py
   ```
4. Follow the menu prompts to perform the desired operations.

---

## CSV File Format

The `data.csv` file should have the following structure:
```csv
id,name,position,salary,email
1,John Doe,Manager,50000,john.doe@example.com
2,Jane Smith,Developer,40000,jane.smith@example.com
```

---

## License
This project is licensed under the MIT License.
