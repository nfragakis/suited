class InvalidVehicleType(Exception):
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        super().__init__(f"Invalid vehicle type provided: {self.vehicle_type}. Options are 'motorcycle', 'car', 'van'")

class NoAvailableSpots(Exception):
    def __init__(self, vehicle_type):
            self.vehicle_type = vehicle_type
            super().__init__(f"No spots available for {self.vehicle_type}.")

class ParkingLot:
    def __init__(self, motorcycle_spots, compact_spots, regular_spots):
        self.spots = {
            'motorcycle': motorcycle_spots,
            'compact': compact_spots,
            'regular': regular_spots
        }
        self.total_spots = sum(self.spots.values())

    def park_vehicle(self, vehicle_type):
        if vehicle_type not in ['motorcycle', 'car', 'van']:
            raise InvalidVehicleType(vehicle_type)

        if vehicle_type == 'motorcycle':
            if self.spots['motorcycle'] > 0:
                self.spots['motorcycle'] -= 1
            elif self.spots['compact'] > 0:
                self.spots['compact'] -= 1
            elif self.spots['regular'] > 0:
                self.spots['regular'] -= 1
            else:
                raise NoAvailableSpots(vehicle_type)

        elif vehicle_type == 'car':
            if self.spots['compact'] > 0:
                self.spots['compact'] -= 1
            elif self.spots['regular'] > 0:
                self.spots['regular'] -= 1
            else:
                raise NoAvailableSpots(vehicle_type)

        elif vehicle_type == 'van':
            if self.spots['regular'] >= 3:
                self.spots['regular'] -= 3
            else:
                raise NoAvailableSpots(vehicle_type)

    def get_available_spots(self):
        return self.spots

    def get_total_spots(self):
        return self.total_spots

    def is_full(self):
        return sum(self.spots.values()) == 0

    def is_empty(self):
        return sum(self.spots.values()) == self.total_spots

    def get_van_spots(self):
        return "A van takes up 3 regular spots."
    
    def get_vehicle_spots(self, vehicle_type):
        if vehicle_type not in ['motorcycle', 'car', 'van']:
            raise InvalidVehicleType(vehicle_type)

        if vehicle_type == 'motorcycle':
            return self.spots['motorcycle'] + self.spots['compact'] + self.spots['regular']
        elif vehicle_type == 'car':
            return self.spots['compact'] + self.spots['regular']
        elif vehicle_type == 'van':
            return self.spots['regular'] // 3

parking_lot = ParkingLot(
    motorcycle_spots=5,
    compact_spots=10,
    regular_spots=20,
)
