"""
All Required APIs for the project

"""

from fastapi import FastAPI
from models.employee import Employee
import helpers.features as f
import helpers.report_functions as rep
from Logger_Configuration.configure_logger import config_logging
from typing import List
from fastapi import HTTPException
from uuid import uuid4
import logging
import os

app = FastAPI()

ROOT_PATH = os.path.dirname(__file__)
LOG_PATH = os.path.join(ROOT_PATH, "logs", "emp_log.log")

# Configuring logging
logger = config_logging(
    logger_name="emp-data",
    formatter="%(asctime)s %(levelname)s %(thread)d - %(message)s",
    log_file_name=LOG_PATH,
    logging_level=logging.INFO,
)


@app.get("/")
async def root():
    """
    Get the root endpoint of the API.

    Returns:
        str: A welcome message for the Employee Management System.
    """
    return "Welcome to Employee Management System"


@app.get("/employees", response_model=List[Employee])
async def get_employees():
    """
    Get a list of employees.

    Returns:
        List[Employee]: A list of Employee objects representing the existing employees.

    Raises:
        HTTPException: If there is an error getting the employees.
    """
    try:
        logger.info("Get employees called")
        return f.get_existing_data()
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Unable to get employees") from e


@app.get("/employees/{id}", response_model=Employee)
async def get_employee(id: str):
    """
    Retrieves an employee with the specified ID.

    Args:
        id (str): The ID of the employee to retrieve.

    Returns:
        Employee: The retrieved employee.

    Raises:
        HTTPException: If there is an error retrieving the employee.

    """
    try:
        logger.info("Get employee by id called")
        return f.get_employee_by_id(id)
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Unable to get employee for given id"
        ) from e


@app.post("/create_employee", response_model=Employee)
async def create_employee(new_employee: Employee):
    """
    Creates a new employee record.

    Args:
        new_employee (Employee): The new employee object to be created.

    Returns:
        Employee: The newly created employee object.

    Raises:
        HTTPException: If there is an error creating the employee record.
    """
    try:
        new_employee.emp_id = str(uuid4())
        f.save_employee(new_employee.__dict__)
        logger.info("Create employee called")
        return new_employee
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Unable to create employee") from e


@app.put("/update_employee/{id}", response_model=Employee)
async def update_employee(id: str, updated_employee: Employee):
    """
    Updates an employee record by ID.

    Parameters:
        id (str): The ID of the employee to be updated.
        updated_employee (Employee): The updated employee object.

    Returns:
        Employee: The updated employee record.

    Raises:
        HTTPException: If there is an error updating the employee record.
    """
    try:
        f.update_employee_by_id(id, updated_employee.__dict__)
        logger.info("update employee called")
        return updated_employee
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Unable to update employee") from e


@app.delete("/delete_employee/{id}", response_model=Employee)
async def delete_employee(id: str):
    """
    Delete an employee by their ID.

    Parameters:
    - id (str): The ID of the employee to be deleted.

    Returns:
    - dict: A dictionary with a message indicating the success of the deletion.

    Raises:
    - HTTPException: If there is an error deleting the employee.
    """
    try:
        employee_data = f.delete_employee_by_id(id)
        logger.info("Employee deleted successfully")
        return employee_data
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Unable to delete employee") from e


@app.get("/department/{name}", response_model=List[Employee])
async def get_employees_by_department(name: str):
    """
    Get a list of employees by department.

    Args:
        name (str): The name of the department.

    Returns:
        List[Employee]: A list of Employee objects representing the employees in the specified department.

    Raises:
        HTTPException: If there is an error getting the employees by department.
    """
    try:
        logger.info("Get employees by department called")
        return f.get_employees_by_department(name)
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Unable to get employees by department"
        ) from e


@app.get("/designation/{name}", response_model=List[Employee])
async def get_employees_by_designation(name: str):
    """
    Get a list of employees by designation.

    Args:
        name (str): The name of the designation.

    Returns:
        List[Employee]: A list of Employee objects representing the employees in the specified designation.

    Raises:
        HTTPException: If there is an error getting the employees by designation.
    """
    try:
        logger.info("Get employees by designation called")
        return f.get_employees_by_designation(name)

    except HTTPException as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Unable to get employees by designation"
        ) from e


@app.get("/skill/{skill_name}", response_model=List[Employee])
async def get_employee_from_skill(skill_name: str):
    """
    Get a list of employees by skill.

    Args:
        skill_name (str): The name of the skill.

    Returns:
        List[Employee]: A list of Employee objects representing the employees with the specified skill.

    Raises:
        HTTPException: If there is an error getting the employees by skill.
    """
    try:
        logger.info("Get employees by skill called")
        return f.get_employees_by_skill(skill_name)
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Unable to get employees by skill"
        ) from e


@app.get("/department_report")
async def get_department_report():
    """
    A function that retrieves a department report.

    Raises:
        HTTPException: If unable to generate the report.
    """
    try:
        rep.department_wise_employee_report()
    except HTTPException as e:
        raise HTTPException(
            status_code=400, detail="Unable to Generate this report"
        ) from e


@app.get("/salary_report")
async def get_salary_report():
    """
    Retrieves the salary report for all departments.

    Raises:
        HTTPException: If there is an error generating the report.
    """
    try:
        rep.department_wise_salary_report()
    except HTTPException as e:
        raise HTTPException(
            status_code=400, detail="Unable to Generate this report"
        ) from e


@app.get("/status/{status}", response_model=List[Employee])
async def filter_employees_by_status(status: str):
    """
    Filters the employees by status and returns a list of matching employees.

    Parameters:
        status (str): The status to filter by.

    Returns:
        List[Employee]: A list of employees with the given status.

    Raises:
        HTTPException: If there is an error fetching the employee records.
    """
    try:
        employees = f.get_employees_by_status(status)
        logger.info("filter employees by status called")
        return employees
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Unable to filter employees by status"
        ) from e


@app.get("/salary/{min_salary}/{max_salary}", response_model=List[Employee])
async def filter_employees_by_salary_range(min_salary: float, max_salary: float):
    """
    Filters the employees by salary range and returns a list of matching employees.

    Args:
        min_salary (float): The minimum salary to filter by.
        max_salary (float): The maximum salary to filter by.

    Returns:
        List[Employee]: A list of employees with salaries within the given range.

    Raises:
        HTTPException: If there is an error fetching the employee records.
    """
    try:
        employees = f.get_employees_by_salary_range(min_salary, max_salary)
        logger.info("filter employees by salary range called")
        return employees
    except HTTPException as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Unable to filter employees by salary range"
        ) from e
