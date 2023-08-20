from tires.tires import Tires

class CarrigonTires(Tires):
    def __init__(self,  tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear_array)