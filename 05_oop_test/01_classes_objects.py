class Car:
    def __init__(self, year, brand, model):
        self.year = year
        self.brand = brand
        self.model = model

mycar = Car(2020, "VW","Tiguan")
print(f"The car {mycar.brand} {mycar.model}")