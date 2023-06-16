from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires_array):
        self.tires_array = tires_array

    def needs_service(self):
       for tire in self.tires_array:
           if tire >= 0.9:
               return True

       return False