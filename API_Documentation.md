
# 🚀 Dokumentasi API Asteroid

## 🖥️ Base URL

```
http://127.0.0.1:5000
```

---

## 📌 Endpoints

### ✅ GET `/`
- **Deskripsi:** Mengecek apakah API aktif.
- **Response:**
  ```
  API Asteroid PostgreSQL Aktif!
  ```

---

### ✅ GET `/asteroids`
- **Deskripsi:** Mengambil seluruh data asteroid.
- **Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "name": "Apophis",
      "size_km": 0.37,
      "hazardous": true
    },
    ...
  ]
  ```

---

### ✅ GET `/asteroids/<id>`
- **Deskripsi:** Mengambil data asteroid berdasarkan ID.
- **Parameter:**
  - `id` (integer): ID asteroid
- **Contoh:** `/asteroids/1`
- **Response jika ditemukan:**
  ```json
  {
    "id": 1,
    "name": "Apophis",
    "size_km": 0.37,
    "hazardous": true
  }
  ```
- **Response jika tidak ditemukan:**
  ```json
  {
    "error": "Asteroid tidak ditemukan"
  }
  ```

---

### ✅ POST `/asteroids`
- **Deskripsi:** Menambahkan data asteroid baru.
- **Header:**
  ```
  Content-Type: application/json
  ```
- **Request Body:**
  ```json
  {
    "name": "Didymos",
    "size_km": 0.78,
    "hazardous": false
  }
  ```
- **Response (201 Created):**
  ```json
  {
    "id": 4,
    "name": "Didymos",
    "size_km": 0.78,
    "hazardous": false
  }
  ```

---

### ✅ DELETE `/asteroids/<id>`
- **Deskripsi:** Menghapus asteroid berdasarkan ID.
- **Contoh:** `/asteroids/2`
- **Response jika berhasil:**
  ```json
  {
    "message": "Asteroid ID 2 dihapus"
  }
  ```
- **Response jika tidak ditemukan:**
  ```json
  {
    "error": "Asteroid tidak ditemukan"
  }
  ```

---

## 📄 Format Data Asteroid

| Kolom       | Tipe    | Keterangan                     |
|-------------|---------|--------------------------------|
| `id`        | Integer | ID unik asteroid               |
| `name`      | String  | Nama asteroid                  |
| `size_km`   | Float   | Ukuran dalam kilometer         |
| `hazardous` | Boolean | Apakah asteroid berbahaya?     |

---

## 🛠️ Status Kode HTTP

| Kode | Arti                    |
|------|-------------------------|
| 200  | OK                      |
| 201  | Created (data ditambahkan) |
| 400  | Bad Request (data salah/tidak lengkap) |
| 404  | Not Found (data tidak ditemukan) |
| 500  | Internal Server Error   |

---

## 🧪 Contoh Tools Uji Coba

- [Postman](https://www.postman.com/)
- `curl` via terminal
- Browser (untuk endpoint GET)

---

## ✍️ Dibuat Oleh

> Backend API untuk proyek asteroid NASA  
> Teknologi: Flask + PostgreSQL  
> Author: _[Nama Anda di sini]_
