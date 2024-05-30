from helpers import functions as f

if __name__ == "__main__":
    while True:
        print("\n**************Welcome to Employee Management System**************")
        print("1. View all Employees")
        print("2. Search Employee by Name")
        print("3. Add Employee")
        print("4. Edit Employee")
        print("5. Remove Employee")
        print("6. Filter Employees by Department name")
        print("7. Filter Employees by Designation")
        print("8. Filter Employees by Status")
        print("9. Filter Employees by Salary Range")
        print("10. Generate Report salary wise")
        print("11. Generate Report department wise")
        print("12. Quit")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                result = f.get_employees()
                print(result)
            case 2:
                e_name = f.take_employee_name()
                result = f.search_employee_by_name(e_name)
                print(result)
            case 3:
                print(f.add_employee())
            case 4:
                print(f.update_employee())
            case 5:
                print(f.delete_employee())
            case 6:
                print(f.filter_employees_by_department())
            case 7:
                print(f.filter_employees_by_designation())
            case 8:
                print(f.filter_employees_by_status())
            case 9:
                print(f.filter_employees_by_salary_range())
            case 10:
                print(f.generate_report_salary_wise())
            case 11:
                print(f.generate_report_department_wise())
            case 12:
                break
            case _:
                print("Invalid choice")
