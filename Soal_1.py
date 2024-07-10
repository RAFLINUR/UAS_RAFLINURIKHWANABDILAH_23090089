Mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    Mahasiswa.append({'NIM': nim, 'Nama': nama})
    tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ")
    if tambah_lagi.lower() != 'ya':
        break
print("Data Mahasiswa:")

for Mahasiswa in Mahasiswa:
    print(f"NIM: {Mahasiswa['NIM']}, Nama: {Mahasiswa['Nama']}")
print("End")
