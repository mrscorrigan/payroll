# class Employee:
#     def __init__(self, id, first, second, years, base):
#         self.emp_id = id
#         self.fname = first
#         self.sname = second
#         self.no_of_years = years
#         self.base_salary = base
#         # self.less_than_three = three
#         # self.less_than_five = five
#         # self.more_than_five = more
#
#
#     def our_staff(self):
#         # def __init__(self, emp_id, fname, sname, no_of_years, base_salary):
#         print " your staff id is %s\n your name is %s %s\n and the number of years you have worked is %s\n and your base salary is %s" \
#                   %(self.emp_id, self.fname, self.sname, self.no_of_years, self.base_salary)
#
#     def salary(self):
#         if our_staff.no_of_years <=3:
#             print "your bonus is 1%"
#         elif our_staff.no_of_years >5:
#             print "your bonus is 25%"
#         #
#         #     # def salary(our_staff):
#         #     #     if our_staff.no_of_years >3 && <=5:
#         #     #         print "your bonus is 5%"
#         #
#         # def salary(self):
#         #     if our_staff.no_of_years >5:
#         #         print "your bonus is 25%"


class Employee:
    # BASE_SALARY = 5000
    employee_number = 0

    def __init__(self, fname, sname, noofyears, base_salary=5000):
        Employee.employee_number += 1
        self.sname = sname
        self.fname = fname
        self.noofyears = noofyears
        self.employee_number = Employee.employee_number
        self.base_salary = base_salary

    ''' calculate the base salary plus
    any bonus based on numer of years worked '''

    def calculate_salary(self):
        bonus = 0
        base_salary = self.base_salary
        if self.noofyears < 3:
            bonus = base_salary * 0.01
        elif self.noofyears <= 5:
            bonus = base_salary * 0.05
        elif self.noofyears > 5:
            bonus = base_salary * 0.25
        return base_salary + bonus

    def get_details(self):
        return ' \n------------------------\n First Name: %s\n Surname %s\n Years Worked: %s\n Employee Number: %s\n Salary: %s\n'  \
               % (self.fname, self.sname, self.noofyears, self.employee_number, self.calculate_salary())


class Developer(Employee):
    lang = "Python"

    def __init__(self, fname, sname, noofyears, lang, base_salary=5000):
        self.lang = lang
        Employee.__init__(self, fname, sname, noofyears, base_salary)

    def calculate_salary(self):
        general_salary = Employee.calculate_salary(self)
        if self.lang.lower() == "python":
            general_salary += general_salary * .1
            old_salary = general_salary - Employee.calculate_salary(self)
            print "---------------------------------------------------\n\n For employee %s %s Python bonus is %s" % (self.fname, self.sname, old_salary)
        return general_salary
