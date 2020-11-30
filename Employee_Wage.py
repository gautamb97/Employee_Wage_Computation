import random


class EmployeeWage:
    print("Welcome to Employee Wage Computation")
    employeeCheck = (random.randint(0, 1))
    EMP_RATE_PER_HOUR = 20
    totalWage = 0
    def checkAttendance(self):
        if EmployeeWage.employeeCheck == 1:
            print("Employee is Present")
        else:
            print("Employee is Absent")

    def dailyWage(self):
        for days in range(21):
            if EmployeeWage.employeeCheck == 1:

                    partTime = (random.randint(0,1))
                    if partTime == 0:
                        empHrs = 4
                    else:
                        empHrs = 8

            else:
                empHrs = 0
            empWage = empHrs * EmployeeWage.EMP_RATE_PER_HOUR
            EmployeeWage.totalWage += empWage

        print("Total wage is: ", EmployeeWage.totalWage)


if __name__=="__main__":

    Employee = EmployeeWage()
    (Employee.checkAttendance())
    (Employee.dailyWage())
