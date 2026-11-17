class Vehicle:
    def __init__(self, vehicleBrand):
        self.vehicleBrand = vehicleBrand

    def showBrand(self):
        print("Brand:", self.vehicleBrand)


class Car(Vehicle):
    def __init__(self, vehicleBrand, carModel):
        super().__init__(vehicleBrand)
        self.carModel = carModel

    def showModel(self):
        self.showBrand()
        print("Model:", self.carModel)


class ElectricCar(Car):
    def __init__(self, vehicleBrand, carModel, batteryCapacity):
        super().__init__(vehicleBrand, carModel)
        self.batteryCapacity = batteryCapacity

    def showCarDetails(self):
        self.showModel()
        print("Battery Capacity:", self.batteryCapacity, "kWh")


myCar = ElectricCar("Tata", "Nexon EV", 40.5)
myCar.showCarDetails()
