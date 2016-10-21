# import staff.employees
# from staff.employees import Employee
#
#
# staffx = Employee("1","Henry","Rollins",2, "5000")
# # staffx.our_staff()
# staffx = Employee("2","David","Lynch",25, "5000")
# # staffx.our_staff()
# staffx = Employee("3","Billy","Corgan",4, "5000")
# # staffx.our_staff()
#
# print staffx.our_staff()
# print staffx.salary()


from staff.employees import Employee
from staff.employees import Developer

emp1 = Employee("Tom", "Tester", 1, 1000)
print emp1.get_details()

emp1 = Employee("Aria", "Tester", 2, 1440)
print emp1.get_details()

dev1 = Developer("Tom", "Ryan", 1, "python", 1000 )
print dev1.get_details()

dev1 = Developer("Tom", "Jones", 1, "Java", 1000 )
print dev1.get_details()



