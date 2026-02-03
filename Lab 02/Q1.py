class Vehicle:
  def __init__(self,id,brand,rent):
    self.id=id
    self.brand=brand
    self.rent=rent

  def display_details(self):
    print("ID: ",self.id)
    print("Brand: ",self.brand)
    print("Rent: ",self.rent)

  def calculate_rent(self,days):
    self.rent= self.rent * days
    print("Total rent: ",self.rent)

v1=Vehicle(123,"BMW",1000)
v2=Vehicle(222,"AUDI", 2000)

v1.display_details()
v2.display_details()

v2.calculate_rent(4)

