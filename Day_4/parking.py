from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, vehicleno: str, number_plate: str, owner_name: str):
        self.vehicleno = vehicleno
        self.number_plate = number_plate
        self.__owner_name = owner_name

    def display(self):
        print("Vehicle number:", self.vehicleno)
        print("Number plate:", self.number_plate)
        print("Owner name:", self.__owner_name)

    def calculate_parking_fee(self, hours: int) -> int:
        rate_per_hour = 20
        return hours * rate_per_hour

    def get_owner(self):
        return self.__owner_name


class ParkingSpot:
    """Represents a single parking spot.

    spot_id: identifier (like 'S1')
    spot_size: one of 'S','M','L','XL'
    """

    def __init__(self, spot_id: str, spot_size: str):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.spot_status = False
        self.parked_vehicle = None

    def can_fit(self, vehicle) -> bool:
        from inspect import isclass

        # Determine allowed sizes per vehicle type
        if isinstance(vehicle, Bike):
            allowed = ["S", "M", "L", "XL"]
        elif isinstance(vehicle, Car):
            allowed = ["M", "L", "XL"]
        elif isinstance(vehicle, SUV):
            allowed = ["L", "XL"]
        elif isinstance(vehicle, Truck):
            allowed = ["XL"]
        else:
            allowed = []
        return self.spot_size in allowed

    def assign_vehicle(self, vehicle) -> bool:
        if self.spot_status:
            print(f"Spot {self.spot_id} is already occupied.")
            return False
        if not self.can_fit(vehicle):
            print(f"Vehicle {vehicle.vehicleno} does not fit in spot {self.spot_id} (size {self.spot_size}).")
            return False
        self.parked_vehicle = vehicle
        self.spot_status = True
        print(f"Vehicle {vehicle.vehicleno} assigned to spot {self.spot_id}.")
        return True

    def remove_vehicle(self):
        if self.spot_status and self.parked_vehicle is not None:
            veh = self.parked_vehicle
            self.parked_vehicle = None
            self.spot_status = False
            print(f"Vehicle {veh.vehicleno} removed from spot {self.spot_id}.")
            return veh
        else:
            print("Parking spot is already empty.")
            return None


class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            status = "Occupied" if spot.spot_status else "Available"
            vehicle = f" ({spot.parked_vehicle.vehicleno})" if spot.parked_vehicle else ""
            print(f"Spot {spot.spot_id}: Size {spot.spot_size}, Status: {status}{vehicle}")

    def park_vehicle(self, vehicle) -> bool:
        for spot in self.spots:
            if not spot.spot_status and spot.can_fit(vehicle):
                return spot.assign_vehicle(vehicle)
        print("No available spots for this vehicle.")
        return False

    def unpark_vehicle(self, vehicle, hours: int):
        for spot in self.spots:
            if spot.spot_status and spot.parked_vehicle is vehicle:
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(f"Parking fee for {hours} hours: ₹{fee}")
                return fee
        print("Vehicle not found in any spot.")
        return None


class Bike(Vehicle):
    def __init__(self, vehicleno: str, number_plate: str, owner_name: str, helmet_required: bool):
        super().__init__(vehicleno, number_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        super().display()
        print("Helmet required:", self.helmet_required)


class Car(Vehicle):
    def __init__(self, vehicleno: str, number_plate: str, owner_name: str, seats: int):
        super().__init__(vehicleno, number_plate, owner_name)
        self.seats = seats

    def display(self):
        super().display()
        print("Number of seats:", self.seats)


class SUV(Vehicle):
    def __init__(self, vehicleno: str, number_plate: str, owner_name: str, four_wheel_drive: bool):
        super().__init__(vehicleno, number_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        super().display()
        print("Four wheel drive:", self.four_wheel_drive)


class Truck(Vehicle):
    def __init__(self, vehicleno: str, number_plate: str, owner_name: str, max_load_capacity: int):
        super().__init__(vehicleno, number_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        super().display()
        print("Max load capacity:", self.max_load_capacity)


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: int):
        raise NotImplementedError


class CashPayment(Payment):
    def process_payment(self, amount: int):
        print(f"Paid ₹{amount} via cash")


class CardPayment(Payment):
    def process_payment(self, amount: int):
        print(f"Paid ₹{amount} via Card")


class UPIPayment(Payment):
    def process_payment(self, amount: int):
        print(f"Paid ₹{amount} via UPI")


if __name__ == "__main__":
    lot = ParkingLot()
    # create a few spots
    lot.add_spot(ParkingSpot("S1", "S"))
    lot.add_spot(ParkingSpot("M1", "M"))
    lot.add_spot(ParkingSpot("L1", "L"))
    lot.add_spot(ParkingSpot("XL1", "XL"))

    # create vehicles
    bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
    car1 = Car("C201", "TS05CD5678", "Priya", 5)
    suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
    truck1 = Truck("T401", "TS11XY4455", "Ravi", 12000)

    # park vehicles
    lot.park_vehicle(bike1)
    lot.park_vehicle(car1)
    lot.park_vehicle(suv1)
    lot.park_vehicle(truck1)

    print("\nCurrent parking status:")
    lot.show_spots()

    # unpark a vehicle and process payment
    hours = 3
    amount = lot.unpark_vehicle(car1, hours)
    if amount is not None:
        payment_method = CardPayment()
        payment_method.process_payment(amount)

    print("\nParking status after unparking:")
    lot.show_spots()


