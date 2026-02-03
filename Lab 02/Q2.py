class Employee:
  def __init__(self,name,id):
    self.name=name
    self.id=id

  def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
  def __init__ (self,name,id,salary):
    super().__init__(name,id)
    self.salary=salary

  def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
  def __init__(self,name,id,hrs_worked,rate):
    super().__init__(name,id)
    self.hrs_worked=hrs_worked
    self.rate=rate

  def calculate_salary(self):
        return self.hrs_worked * self.rate

full1 = FullTimeEmployee("Sameed", 1, 30000)
part1 = PartTimeEmployee("Ahmed", 2, 20, 1300)
print("Full-Time Employee Salary:", full1.calculate_salary())
print("Part-Time Employee Salary:", part1.calculate_salary())


