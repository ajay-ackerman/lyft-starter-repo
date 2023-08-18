from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return  Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date))
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date))
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on),SpindlerBattery(current_date, last_service_date))
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date))
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return  Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date))