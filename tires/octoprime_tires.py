from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires_array):
        self.tires_array = tires_array

    def needs_service(self):
        sum = 0
        for tire in self.tires_array:
            sum += tire

        if sum >= 3:
            return True
        else:
            return False