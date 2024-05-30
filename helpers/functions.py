# functions.py

import json
import requests
from models.employee import Employee

base_url = "http://localhost:8000"


def take_employee_id():
    """
    Takes user input for the employee id and returns it.
    """
    id = input("Enter the employee id: ")
    return id


def add_employee():
    """
    Adds a new employee to the system.

    Returns:
        - If successful, the function returns the JSON response from the API call.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Create an Employee object with user input
    emp = Employee(
        emp_name=input("Enter the employee name: "),
        emp_gender=input("Enter the employee gender: "),
        emp_status=input("Enter the employee status: "),
        emp_email=input("Enter the employee email: "),
        emp_address=input("Enter the employee address: "),
        emp_phone=input("Enter the employee phone: "),
        emp_designation=input("Enter the employee designation: "),
        emp_department=input("Enter the employee department: "),
        emp_salary=float(input("Enter the employee salary: ")),
        emp_skills=list(input("Enter skills separated by space: ").split()),
    )

    # Convert the Employee object to a dictionary
    employee_data = emp.dict()

    # Make a POST request to the API endpoint
    response = requests.post(f"{base_url}/create_employee", json=employee_data)

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"


def check_response(response):
    """
    Check the status code of the response and return True if it is 200, otherwise return False.

    Parameters:
        response (object): The response object to check the status code of.

    Returns:
        bool: True if the status code is 200, False otherwise.
    """
    if response.status_code == 200:
        return True
    else:
        return False


def get_employees():
    """
    Get a list of employees from the server.

    Returns:
        If the request is successful, returns a list of employees in JSON format.
        If the request is unsuccessful, returns a string indicating that no employees were found.
    """
    # Make a GET request to the API endpoint
    response = requests.get(f"{base_url}/employees")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "No employees found"


def get_employee_by_id(id):
    """
    Get an employee by id from the server.

    Parameters:
        id (str): The employee id to search for.

    Returns:
        If the request is successful and the employee is found, returns the employee details in JSON format.
        If the request is unsuccessful or the employee is not found, returns a string indicating the error.
    """
    # Make a GET request to the API endpoint with the id as a query parameter
    response = requests.get(f"{base_url}/employees/{id}")

    # Check the status code and return the result
    if check_response(response):
        # Check if the response is empty or not
        if response.json():
            return response.json()
        else:
            return "Employee not found"
    else:
        return "Something went wrong"


def update_employee():
    """
    Updates an existing employee in the system.

    Returns:
        - If successful, the function returns the JSON response from the API call.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Take the employee id from the user
    id = take_employee_id()

    # Get the current employee details by id
    current_employee = get_employee_by_id(id)

    # Check if the employee exists or not
    if (
        current_employee == "Employee not found"
        or current_employee == "Something went wrong"
    ):
        return current_employee
    else:
        # Create a new Employee object with the current details
        new_employee = Employee(**current_employee)

        # Ask the user which fields to update and update the Employee object accordingly
        print(
            "Enter the new values for the fields you want to update. Leave blank for no change."
        )
        new_name = input("Enter the new name: ")
        if new_name:
            new_employee.emp_name = new_name
        new_gender = input("Enter the new gender: ")
        if new_gender:
            new_employee.emp_gender = new_gender
        new_status = input("Enter the new status: ")
        if new_status:
            new_employee.emp_status = new_status
        new_email = input("Enter the new email: ")
        if new_email:
            new_employee.emp_email = new_email
        new_address = input("Enter the new address: ")
        if new_address:
            new_employee.emp_address = new_address
        new_phone = input("Enter the new phone: ")
        if new_phone:
            new_employee.emp_phone = new_phone
        new_designation = input("Enter the new designation: ")
        if new_designation:
            new_employee.emp_designation = new_designation
        new_department = input("Enter the new department: ")
        if new_department:
            new_employee.emp_department = new_department
        new_salary = input("Enter the new salary: ")
        if new_salary:
            new_employee.emp_salary = float(new_salary)
        new_skills = input("Enter the new skills separated by space: ")
        if new_skills:
            new_employee.emp_skills = list(new_skills.split())

        # Convert the updated Employee object to a dictionary
        employee_data = new_employee.dict()

        # Make a PUT request to the API endpoint with the id as a query parameter and the employee data as the body
        response = requests.put(f"{base_url}/update_employee/{id}", json=employee_data)

        # Check the status code and return the result
        if check_response(response):
            return response.json()
        else:
            return "Something went wrong"


def delete_employee():
    """
    Deletes an existing employee from the system.

    Returns:
        - If successful, the function returns the JSON response from the API call.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Take the employee id from the user
    id = take_employee_id()

    # Make a DELETE request to the API endpoint with the id as a query parameter
    response = requests.delete(f"{base_url}/delete_employee/{id}")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"


def filter_employees_by_department():
    """
    Filters the employees by gender and returns a list of matching employees.

    Returns:
        - If successful, the function returns a list of employees in JSON format.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Take the name from the user
    name = input("Enter the department name to filter by: ")

    # Make a GET request to the API endpoint with the gender as a query parameter
    response = requests.get(f"{base_url}/department/{name}")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"


def filter_employees_by_status():
    """
    Filters the employees by status and returns a list of matching employees.

    Returns:
        - If successful, the function returns a list of employees in JSON format.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Take the status from the user
    status = input("Enter the status to filter by: ")

    # Make a GET request to the API endpoint with the status as a query parameter
    response = requests.get(f"{base_url}/status/{status}")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"


def filter_employees_by_designation():
    """
    Filters the employees by designation and returns a list of matching employees.

    Returns:
        - If successful, the function returns a list of employees in JSON format.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Take the status from the user
    designation = input("Enter the designation to filter by: ")

    # Make a GET request to the API endpoint with the status as a query parameter
    response = requests.get(f"{base_url}/designation/{designation}")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"


def filter_employees_by_salary_range():
    """
    Filters the employees by salary range and returns a list of matching employees.

    Returns:
        - If successful, the function returns a list of employees in JSON format.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Take the minimum and maximum salary from the user
    min_salary = float(input("Enter the minimum salary: "))
    max_salary = float(input("Enter the maximum salary: "))

    # Make a GET request to the API endpoint with the min_salary and max_salary as query parameters
    response = requests.get(f"{base_url}/salary/{min_salary}/{max_salary}")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"


def generate_report_salary_wise():
    """
    Generates a report of the number of employees in each salary range.

    Returns:
        - If successful, the function returns a dictionary of salary ranges and counts in JSON format.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Make a GET request to the API endpoint
    response = requests.get(f"{base_url}/salary_report")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"


def generate_report_department_wise():
    """
    Generates a report of the number of employees in each department.

    Returns:
        - If successful, the function returns a dictionary of departments and counts in JSON format.
        - If unsuccessful, the function returns the string "Something went wrong".
    """
    # Make a GET request to the API endpoint
    response = requests.get(f"{base_url}/department_report")

    # Check the status code and return the result
    if check_response(response):
        return response.json()
    else:
        return "Something went wrong"
