from queue import Queue

def main():
    queue = Queue()

    while True:
        print("\nSistem Antrian Restoran")
        print("1. Tambah Pesanan (Enqueue)")
        print("2. Ambil Pesanan (Dequeue)")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            order = input("Masukkan nama pesanan: ")
            queue.enqueue(order)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.display()
        elif choice == '4':
            print("Terima kasih telah menggunakan sistem antrian restoran.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
