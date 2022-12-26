
print('the first class')

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{first_name}.{last_name}@company.com'

    def fullname(self):
        print(f'{self.first_name} {self.last_name}')

emp1 = Employee('Nayan', 'Rathod', 80000)
emp2 = Employee('Sonika', 'Singh', 40000)

print(emp1.email)
print(emp2.email)

emp1.fullname()
emp2.fullname()
#