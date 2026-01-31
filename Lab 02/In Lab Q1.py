class Lights:

  def __init__(self,name,switch):
    self.name=name
    self.switch=switch

    if(self.switch):
      print(self.name, " is ON")
    else:
      print(self.name, " is OFF")

  
  def LightSwitch(self,switch):
    self.switch=switch

    if(self.switch):
      print(self.name, " is ON")
    else:
      print(self.name, " is OFF")

l1=Lights("Bedroom Light",True)
l2=Lights("Lounge light", False)

l2.LightSwitch(True)
