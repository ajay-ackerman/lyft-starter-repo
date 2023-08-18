from abc import abstractclassmethod


class Serviceable:
    @abstractclassmethod
    def needs_service(self):bool