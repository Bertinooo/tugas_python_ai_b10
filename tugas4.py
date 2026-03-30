# ==========================================
# TUGAS 4: STRUKTUR DATA PYTHON
# ==========================================

# --- 1. LIST - AKSES & MANIPULASI ---
print("=== 1. LIST ===")
my_list = ["Python", 2026, 3.14, "Unity", True, 99] # >= 6 elemen campuran
print(f"List awal:\n{my_list}")
print(f"Elemen pertama: {my_list[0]} | Elemen terakhir: {my_list[-1]}")
print(f"Slicing [1:5:2]: {my_list[1:5:2]}")

print("\nManipulasi List:")
my_list.append("Item Baru")
print(f"Setelah append(): {my_list}")

my_list.insert(2, "Sisipan")
print(f"Setelah insert(): {my_list}")

my_list.extend([88, "Ekstra"])
print(f"Setelah extend(): {my_list}")

my_list.pop()
print(f"Setelah pop() (hapus item terakhir): {my_list}")

my_list.remove(3.14)
print(f"Setelah remove(3.14): {my_list}\n")


# --- 2. TUPLE - IMMUTABILITY & UNPACKING ---
print("=== 2. TUPLE ===")
my_tuple = ("HTML", "CSS", "JS", "C#", "Laravel") # >= 5 elemen
print(f"Tuple awal: {my_tuple}")
print(f"Panjang tuple: {len(my_tuple)}")
print(f"Akses indeks ke-3: {my_tuple[3]}")

# Unpacking menggunakan *rest
a, b, *rest = my_tuple
print(f"Unpacking -> a: {a}, b: {b}, sisa (*rest): {rest}\n")


# --- 3. SET - KEUNIKAN & OPERASI HIMPUNAN ---
print("=== 3. SET ===")
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")

print(f"Union (|): {set_A | set_B}")
print(f"Intersection (&): {set_A & set_B}")
print(f"Difference A - B (-): {set_A - set_B}")
print(f"Symmetric Difference (^): {set_A ^ set_B}")

# Bukti duplikat hilang
set_duplikat = {1, 1, 2, 2, 3, 3, 3}
print(f"Set dengan input duplikat {{1, 1, 2, 2, 3, 3, 3}} menjadi: {set_duplikat}\n")


# --- 4. DICTIONARY - KEY/VALUE DASAR ---
print("=== 4. DICTIONARY ===")
mhs = {
    "nama": "Bertino",
    "nim": "12345678",
    "angkatan": 2024,
    "kota": "Jakarta"
}
print(f"Dict awal: {mhs}")

mhs["jurusan"] = "Informatika" # Tambah key baru
mhs["kota"] = "Bandung"        # Ubah nilai key
del mhs["angkatan"]          # Hapus key
print(f"Dict setelah operasi: {mhs}")

print(f"Keys: {list(mhs.keys())}")
print(f"Values: {list(mhs.values())}")
print(f"Items: {list(mhs.items())}")

print("Iterasi key: value ->")
for key, value in mhs.items():
    print(f"- {key}: {value}")
print()


# --- 5. NESTED STRUCTURES ---
print("=== 5. NESTED STRUCTURES ===")
daftar_buku = [
    {"judul": "Belajar Python", "penulis": "Andi", "tahun": 2020},
    {"judul": "Mastering Unity", "penulis": "Budi", "tahun": 2023},
    {"judul": "Web dengan Laravel", "penulis": "Cici", "tahun": 2019},
    {"judul": "Data Science", "penulis": "Deni", "tahun": 2024}
]

print("Semua Judul Buku:")
for buku in daftar_buku:
    print(f"- {buku['judul']}")

# Filter buku terbit >= 2022
buku_baru = [buku for buku in daftar_buku if buku["tahun"] >= 2022]
print(f"Buku terbit >= 2022: {buku_baru}\n")


# --- 6. COMPREHENSION & UTILITAS ---
print("=== 6. COMPREHENSION ===")
# List comprehension genap & kuadrat (1-20)
list_genap = [x for x in range(1, 21) if x % 2 == 0]
list_kuadrat = [x**2 for x in range(1, 21)]
print(f"List Genap (1-20): {list_genap}")
print(f"List Kuadrat (1-20): {list_kuadrat}")

# Dict comprehension mapping (1-10)
dict_mapping = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print(f"Dict Mapping: {dict_mapping}")

# Set comprehension huruf unik
kalimat = "Belajar AI itu asik"
# Mengambil huruf kecil, mengabaikan spasi
set_huruf = {huruf.lower() for huruf in kalimat if huruf != " "}
print(f"Set huruf unik dari kalimat: {set_huruf}\n")


# --- 7. KEANGGOTAAN & PENCARIAN SEDERHANA ---
print("=== 7. KEANGGOTAAN & PENCARIAN ===")
# Cek keanggotaan list dan set
cek_list = "Unity" in my_list
cek_set = 99 in set_A
print(f"Apakah 'Unity' ada di my_list? {cek_list}")
print(f"Apakah angka 99 ada di set_A? {cek_set}")

# Melaporkan posisi dengan index() dan in
item_dicari = "CSS"
if item_dicari in my_tuple:
    posisi = my_tuple.index(item_dicari)
    print(f"Item '{item_dicari}' ditemukan di tuple pada indeks ke-{posisi}.")
else:
    print(f"Item '{item_dicari}' tidak ditemukan.")
