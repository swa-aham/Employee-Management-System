import json
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(project_root, "data", "emp.json")


def get_existing_data():
    """this function will read the data from the file"""
    if os.path.exists(JSON_PATH) and os.path.getsize(JSON_PATH) > 0:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    else:
        return []


def save_employee(new_employee):
    """this function will save the employee data in the file"""
    existing_data = get_existing_data()
    existing_data.append(new_employee)
    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=2)


def get_employee_by_id(id: str):
    """this function will get the employee data by id"""
    existing_data = get_existing_data()
    for employee in existing_data:
        if employee["emp_id"] == id:
            return employee


def update_employee_by_id(id: str, updated_employee):
    """this function will update the employee data by id"""
    existing_data = get_existing_data()
    for index, employee in enumerate(existing_data):
        if employee["emp_id"] == id:
            # Exclude updating emp_id field
            updated_data = {
                key: value for key, value in updated_employee.items() if key != "emp_id"
            }
            existing_data[index].update(updated_data)
            break

    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=2)


def delete_employee_by_id(id: str):
    """this function will delete the employee data by id"""
    existing_data = get_existing_data()
    for index, employee in enumerate(existing_data):
        if employee["emp_id"] == id:
            employee_data = existing_data[index]
            existing_data.remove(existing_data[index])
            break
    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=2)

    return employee_data


def get_employees_by_department(department: str):
    """this function will get the employee data by department"""
    existing_data = get_existing_data()
    department_employee = []
    for employee in existing_data:
        if employee.get("emp_department") == department:
            department_employee.append(employee)

    return department_employee


def get_employees_by_designation(designation: str):
    """this function will get the employee data by designation"""
    existing_data = get_existing_data()
    designation_employee = []
    for employee in existing_data:
        if employee.get("emp_designation") == designation:
            designation_employee.append(employee)

    return designation_employee


def get_employees_by_skill(skill: str):
    """this function will get the employee data by skill"""
    existing_data = get_existing_data()
    skill_employee = []
    for employee in existing_data:
        if skill in employee.get("emp_skills"):
            skill_employee.append(employee)

    return skill_employee


def get_employees_by_gender(gender: str):
    """this function will get the employee data by gender"""
    existing_data = get_existing_data()
    gender_employee = []
    for employee in existing_data:
        if employee.get("emp_gender") == gender:
            gender_employee.append(employee)

    return gender_employee


def get_employees_by_status(status: str):
    """this function will get the employee data by status"""
    existing_data = get_existing_data()
    status_employee = []
    for employee in existing_data:
        if employee.get("emp_status") == status:
            status_employee.append(employee)

    return status_employee


def get_employees_by_salary_range(min_salary: float, max_salary: float):
    """this function will get the employee data by salary range"""
    existing_data = get_existing_data()
    salary_employee = []
    for employee in existing_data:
        if min_salary <= employee.get("emp_salary") <= max_salary:
            salary_employee.append(employee)

    return salary_employee


def generate_report_skill_wise():
    """this function will generate a report of the number of employees having each skill"""
    existing_data = get_existing_data()
    skill_count = {}
    for employee in existing_data:
        for skill in employee.get("emp_skills"):
            if skill in skill_count:
                skill_count[skill] += 1
            else:
                skill_count[skill] = 1

    return skill_count


def generate_report_department_wise():
    """this function will generate a report of the number of employees in each department"""
    existing_data = get_existing_data()
    department_count = {}
    for employee in existing_data:
        department = employee.get("emp_department")
        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1

    return department_count


def generate_report_salary_wise():
    """this function will generate a report of the number of employees in each salary range"""
    existing_data = get_existing_data()
    salary_ranges = [
        (0, 20000),
        (20000, 40000),
        (40000, 60000),
        (60000, 80000),
        (80000, 100000),
        (100000, float("inf")),
    ]
    salary_count = {}
    for employee in existing_data:
        salary = employee.get("emp_salary")
        for min_salary, max_salary in salary_ranges:
            if min_salary <= salary < max_salary:
                range_str = f"{min_salary}-{max_salary}"
                if range_str in salary_count:
                    salary_count[range_str] += 1
                else:
                    salary_count[range_str] = 1
                break

    return salary_count
