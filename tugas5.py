# ==========================================
# TUGAS 5: FUNCTION & CLASS
# ==========================================

# --- FUNCTION ---

def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if not angka:  # Jika list kosong
        return 0.0
    # Mengembalikan rata-rata dengan 2 angka di belakang koma
    return round(sum(angka) / len(angka), 2)


# --- CLASS STUDENT ---

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []  # Awal list kosong

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        # Menggunakan function rata_rata() yang dibuat di atas
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        # Mengembalikan string ringkas
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"


# --- DEMO ---

if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    
    # Panggil dan cetak hasil function
    print(greet("Arifian"))
    print(f"tambah(5, 7) = {tambah(5, 7)}")
    print(f"tambah(10)   = {tambah(10)}")
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([])            = {rata_rata([])}")
    
    print("\n=== CLASS STUDENT ===")
    
    # Buat 2 mahasiswa
    mhs1 = Student("Budi", "A123")
    mhs2 = Student("Siti", "B456")
    
    # Isi beberapa nilai via tambah_nilai
    mhs1.tambah_nilai(80.5)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(78.5)
    
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(55.5)
    
    # Cetak objek, rata-rata, dan status kelulusan Mahasiswa 1
    print("--- Data Mahasiswa 1 ---")
    print(mhs1)  # Akan otomatis memanggil __str__
    print(f"Rata-rata : {mhs1.rata_nilai()}")
    print(f"Status    : {mhs1.status()}")
    
    # Cetak objek, rata-rata, dan status kelulusan Mahasiswa 2
    print("\n--- Data Mahasiswa 2 ---")
    print(mhs2)  # Akan otomatis memanggil __str__
    print(f"Rata-rata : {mhs2.rata_nilai()}")
    print(f"Status    : {mhs2.status()}")
