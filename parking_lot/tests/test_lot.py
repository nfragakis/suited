import requests 

def test_initialization():
    response = requests.get('http://localhost:8296/api/v1/total_spots')
    assert response.status_code == 200
    assert response.json()['total_spots'] == 35  # 5 motorcycle spots + 10 compact spots + 20 regular spots


def test_parking():
    response = requests.post('http://localhost:8296/api/v1/park_vehicle/motorcycle')
    assert response.json()['success'] == True
    response = requests.post('http://localhost:8296/api/v1/park_vehicle/car')
    assert response.json()['success'] == True
    response = requests.post('http://localhost:8296/api/v1/park_vehicle/van')
    assert response.json()['success'] == True

def test_available_spots():
    response = requests.get('http://localhost:8296/api/v1/available_spots')
    print(response.json())
    assert sum(response.json()['available_spots'].values()) == 30
    assert response.json()['available_spots']['motorcycle'] == 4
    assert response.json()['available_spots']['compact'] == 9
    assert response.json()['available_spots']['regular'] == 17

def test_full_empty():
    response = requests.get('http://localhost:8296/api/v1/is_empty')
    assert response.json()['is_empty'] == False

    response = requests.get('http://localhost:8296/api/v1/is_full')
    assert response.json()['is_full'] == False
    

def test_remaining_spots():
    response = requests.get('http://localhost:8296/api/v1/vehicle_spots/motorcycle')
    assert response.json()['vehicle_spots'] == 30

    response = requests.get('http://localhost:8296/api/v1/vehicle_spots/car')
    assert response.json()['vehicle_spots'] == 26

    response = requests.get('http://localhost:8296/api/v1/vehicle_spots/van')
    assert response.json()['vehicle_spots'] == 5
