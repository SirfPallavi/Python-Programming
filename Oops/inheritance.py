class Car:
    color ="Blue"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotoCa(Car):
    def __init__(self,name,model):
        self.name = name
        self.model = model

class HondaCar(ToyotoCa):
    def __init__(self,brand,year):
        # super().__init__(brand, year)
        self.brand=brand
        self.year=year

car = ToyotoCa("fortuner","2021")
print(car.color)
car.start()
car1 = ToyotoCa("prius","2020")
print(car1.name,car1.model)
car1 = HondaCar("civic","2022")
print(car1.brand,car1.year)
car1.start()
 

