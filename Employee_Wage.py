import random


class EmployeeWage:
    print("Welcome to Employee Wage Computation")
    employeeCheck = (random.randint(0, 1))
    def checkAttendance(self):
        if EmployeeWage.employeeCheck == 1:
            print("Employee is Present")
        else:
            print("Employee is Absent")

    def dailyWage(self):
        EMP_RATE_PER_HOUR = 20
        if EmployeeWage.employeeCheck == 1:
            partTime = (random.randint(0,1))
            if partTime == 0:
                empHrs = 4
                print("Employee is part time worker")
            else:
                empHrs = 8
                print("Employee is full time worker")
        else:
            empHrs = 0
        empWage = empHrs * EMP_RATE_PER_HOUR
        print("Employee daily Wage is : ",empWage)

if __name__=="__main__":

    Employee = EmployeeWage()
    (Employee.checkAttendance())
    (Employee.dailyWage())