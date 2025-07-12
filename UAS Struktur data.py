# Aplikasi Catatan Pinjaman Teman (Utang Piutang)
# Fitur: Tambah Data, Tampilkan Semua Data, Hapus Data
# Struktur Data: Linked List dan HashMap (Dictionary)

import csv

class Node:
    def __init__(self, nama, jumlah, tanggal, keterangan):
        self.nama = nama
        self.jumlah = jumlah
        self.tanggal = tanggal
        self.keterangan = keterangan
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_data(self, nama, jumlah, tanggal, keterangan):
        node_baru = Node(nama, jumlah, tanggal, keterangan)
        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan_semua(self):
        current = self.head
        if current is None:
            print("\nTidak ada data utang.\n")
            return
        print("\nDaftar Utang:")
        while current:
            print(f"- {current.nama} | {current.jumlah} | {current.tanggal} | {current.keterangan}")
            current = current.next
        print()

    def hapus_data(self, nama):
        current = self.head
        prev = None
        while current:
            if current.nama == nama:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

hashmap = {}
linked_list = LinkedList()

def simpan_csv():
    with open("data_utang.csv", "w", newline="") as file:
        writer = csv.writer(file)
        current = linked_list.head
        while current:
            writer.writerow([current.nama, current.jumlah, current.tanggal, current.keterangan])
            current = current.next

while True:
    print("\n=== Aplikasi Catatan Pinjaman Teman ===")
    print("1. Tambah Data Utang")
    print("2. Tampilkan Semua Data")
    print("3. Hapus Data")
    print("0. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama: ")
        jumlah = input("Jumlah: ")
        tanggal = input("Tanggal (YYYY-MM-DD): ")
        keterangan = input("Keterangan: ")
        linked_list.tambah_data(nama, jumlah, tanggal, keterangan)
        hashmap[nama] = True
        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        linked_list.tampilkan_semua()

    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin dihapus: ")
        if hashmap.get(nama):
            berhasil = linked_list.hapus_data(nama)
            if berhasil:
                del hashmap[nama]
                print("Data berhasil dihapus.")
            else:
                print("Data tidak ditemukan di linked list.")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == "0":
        simpan_csv()
        print("Data disimpan. Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
