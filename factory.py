from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarrigonTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage , tires_wear_array):
        return  Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),CarrigonTires(tires_wear_array))
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage ,tires_wear_array):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),OctoprimeTires(tires_wear_array))
    
    def create_palindrome(current_date, last_service_date, warning_light_on ,tires_wear_array):
        return Car(SternmanEngine(warning_light_on),SpindlerBattery(current_date, last_service_date),CarrigonTires(tires_wear_array))
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage  ,tires_wear_array):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),OctoprimeTires(tires_wear_array))
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage ,tires_wear_array):
        return  Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date) , CarrigonTires(tires_wear_array))