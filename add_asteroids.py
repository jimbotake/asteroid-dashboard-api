import requests

URL = "http://127.0.0.1:5000/asteroids"

asteroids_data = [
    {"name": "Apophis", "size_km": 0.37, "hazardous": True},
    {"name": "Bennu", "size_km": 0.49, "hazardous": True},
    {"name": "Florence", "size_km": 4.4, "hazardous": False},
]

for asteroid in asteroids_data:
    response = requests.post(URL, json=asteroid)
    if response.status_code == 201:
        print(f"Berhasil tambah: {asteroid['name']}")
    else:
        print(f"Gagal tambah: {asteroid['name']} - {response.text}")
