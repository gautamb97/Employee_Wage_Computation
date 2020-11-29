import random


class EmployeeWage:
    print("Welcome to Employee Wage Computation")
    def checkAttendance(self):
        if(random.randint(0,1)) == 1:
            print("Employee is Present")
        else:
            print("Employee is Absent")

if __name__=="__main__":

    Employee = EmployeeWage()
    (Employee.checkAttendance())
