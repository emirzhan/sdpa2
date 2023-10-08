from abc import ABC, abstractmethod

class CarRental(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class BasicCarRental(CarRental):
    def get_description(self):
        return "Basic Car Rental"

    def get_cost(self):
        return 100

class GPSDecorator(CarRental):
    def __init__(self, car_rental):
        self.car_rental = car_rental

    def get_description(self):
        return self.car_rental.get_description() + ", GPS"

    def get_cost(self):
        return self.car_rental.get_cost() + 10

class ChildSeatDecorator(CarRental):
    def __init__(self, car_rental):
        self.car_rental = car_rental

    def get_description(self):
        return self.car_rental.get_description() + ", Child Seat"

    def get_cost(self):
        return self.car_rental.get_cost() + 5

car_rental = BasicCarRental()

car_rental_with_gps = GPSDecorator(car_rental)
car_rental_with_child_seat = ChildSeatDecorator(car_rental)

print("Basic Car Rental:", car_rental.get_description(), "| Cost:", car_rental.get_cost())
print("Car Rental with GPS:", car_rental_with_gps.get_description(), "| Cost:", car_rental_with_gps.get_cost())
print("Car Rental with Child Seat:", car_rental_with_child_seat.get_description(), "| Cost:", car_rental_with_child_seat.get_cost())
