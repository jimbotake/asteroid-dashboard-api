import requests
import csv

URL = "http://127.0.0.1:5000/asteroids"

response = requests.get(URL)

if response.status_code == 200:
    asteroids = response.json()

    # Nama file CSV
    filename = "asteroids.csv"

    # Menentukan nama kolom (header)
    fieldnames = ["id", "name", "size_km", "hazardous"]

    # Menulis ke CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for a in asteroids:
            writer.writerow(a)

    print(f"Data asteroid berhasil disimpan ke '{filename}'")
else:
    print(f"Gagal mengambil data: {response.status_code} - {response.text}")
