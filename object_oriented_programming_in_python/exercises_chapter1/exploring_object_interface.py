# Created the classs for practice
class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def give_raise(self, amount):
        self.salary += amount

mystery = Employee('Natasha Ting', 73500)


# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)