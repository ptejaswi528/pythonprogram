class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
ob=Employee("Alice",50000)
ob.display()
ob1=Manager("Bob",80000,"Sales")
ob1.display()