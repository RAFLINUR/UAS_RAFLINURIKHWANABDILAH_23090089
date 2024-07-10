class queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan '{item}' telah ditambahkan ke antrian.")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Pesanan '{item}' telah diambil dari antrian.")
            return item
        else:
            print("Antrian kosong, tidak ada pesanan yang dapat diambil.")
            return None

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            print("Daftar pesanan dalam antrian:")
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item}")
        else:
            print("Antrian kosong.")