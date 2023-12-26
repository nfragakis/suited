from app import core

def available_spots():
    spots = core.parking_lot.get_available_spots()
    return {'available_spots': spots}

def total_spots():
    spots = core.parking_lot.get_total_spots()
    return {'total_spots': spots}

def park_vehicle(vehicle_type):
    try:
        core.parking_lot.park_vehicle(vehicle_type)
    except core.InvalidVehicleType as e:
        return {'error': str(e)}, 400
    except core.NoAvailableSpots as e:
        return {'error': str(e)}, 409

    return {'success': True}

def is_full():
    full = core.parking_lot.is_full()
    return {'is_full': full}

def is_empty():
    empty = core.parking_lot.is_empty()
    return {'is_empty': empty}

def van_spots():
    spots = core.parking_lot.get_van_spots()
    return {'van_spots': spots}

def vehicle_spots(vehicle_type):
    try:
        spots = core.parking_lot.get_vehicle_spots(vehicle_type)
    except core.InvalidVehicleType as e:
        return {'error': str(e)}, 400

    return {'vehicle_spots': spots}