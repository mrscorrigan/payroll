class Employee:
    def __init__(self, id, first, second, years, base):
        self.emp_id = id
        self.fname = first
        self.sname = second
        self.no_of_years = years
        self.base_salary = base
        # self.less_than_three = three
        # self.less_than_five = five
        # self.more_than_five = more


    def our_staff(self):
        # def __init__(self, emp_id, fname, sname, no_of_years, base_salary):
        print " your staff id is %s\n your name is %s %s\n and the number of years you have worked is %s\n and your base salary is %s" \
                  %(self.emp_id, self.fname, self.sname, self.no_of_years, self.base_salary)

    def salary(self):
        if self.no_of_years <=3:
            print "your bonus is 1%"

            # def salary(our_staff):
            #     if our_staff.no_of_years >3 && <=5:
            #         print "your bonus is 5%"

    # def salary(self):
    #     if self.no_of_years >5:
    #         print "your bonus is 25%"


staffx = Employee("1","Henry","Rollins",2, "5000")
staffx.our_staff()
staffx = Employee("2","David","Lynch",25, "5000")
staffx.our_staff()
staffx = Employee("3","Billy","Corgan",4, "5000")
staffx.our_staff()

print staffx.our_staff()
print staffx.salary()
