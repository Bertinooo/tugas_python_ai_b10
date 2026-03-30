# 1. Deklarasi Variabel dan Tipe Data
nama_karakter = "Bertino"                 # string
level_sekarang = 42                       # integer
win_rate = 75.5                           # float
is_student = True                         # boolean
game_list = ["Clash Royale", "Honkai: Star Rail", "Roblox", "GTA V", "Unity Engine"] # list

print("--- 1. Variabel & Tipe Data ---")
print("Nama:", nama_karakter)
print("Level:", level_sekarang)
print("Win Rate:", win_rate)
print("Mahasiswa:", is_student)
print("Daftar Game:", game_list)
print("\n")

# 2. Manipulasi String
print("--- 2. Manipulasi String ---")
judul_tugas = "Belajar Python AI itu Seru"
print("Teks Asli:", judul_tugas)
print("Panjang string (len):", len(judul_tugas))
print("Huruf Besar (upper):", judul_tugas.upper())
print("Huruf Kecil (lower):", judul_tugas.lower())
print("Gabung string:", nama_karakter + " sedang " + judul_tugas.lower())
print("\n")

# 3. Operasi Matematika Sederhana
print("--- 3. Operasi Matematika ---")
a = 15
b = 4
print(f"Nilai a = {a}, b = {b}")
print("Penjumlahan (+):", a + b)
print("Pengurangan (-):", a - b)
print("Perkalian (*):", a * b)
print("Pembagian (/):", a / b)
print("Pembagian Bulat (//):", a // b)
print("Sisa Bagi/Modulus (%):", a % b)
print("\n")

# 4. List dan Akses Elemen
print("--- 4. List & Akses Elemen ---")
print("List awal:", game_list)
print("Menampilkan game urutan kedua (indeks 1):", game_list[1])

# Menambahkan item baru
game_list.append("Genshin Impact") 
print("Setelah ditambah (append):", game_list)

# Menghapus item (menghapus item terakhir dengan pop)
game_list.pop() 
print("Setelah dihapus (pop):", game_list)
print("\n")

# 5. Penggunaan Input dari User
print("--- 5. Input User ---")
input_nama = input("Masukkan nama Anda: ")
input_umur = input("Masukkan umur Anda: ")
print(f"Halo, nama saya {input_nama} dan umur saya {input_umur} tahun.")
