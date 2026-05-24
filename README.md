**JUDUL: IMPLEMENTASI BINARY SEARCH TREE PADA DAFTAR NILAI MAHASISWA**

**DESKRIPSI SINGKAT:**

Program ini merupakan implementasi Binary Search Tree (BST)
untuk pengelolaan data nilai mahasiswa secara terstruktur. 
Sistem dapat melakukan proses penambahan nilai, penghapusan nilai, 
menampilkan seluruh data nilai berdasarkan urutan level pohon, menghitung tinggi pohon,
serta mencari nilai successor dan predecessor dari suatu data. Struktur BST digunakan
untuk menyusun nilai secara terurut, di mana nilai yang lebih kecil ditempatkan di sisi kiri 
dan nilai yang lebih besar ditempatkan di sisi kanan, sehingga proses pencarian dan pengolahan 
data menjadi lebih efisien dan mudah dilakukan.

**SOURCE KODE & PENJELASAN**

<img width="267" height="105" alt="Screenshot 2026-05-24 121123" src="https://github.com/user-attachments/assets/ce6256fd-3378-4422-ade8-293fd26bc295" />

class Node:
Baris ini digunakan untuk membuat class bernama Node yang berfungsi sebagai simpul atau node pada Binary Search Tree.

def __init__(self, key):
Baris ini merupakan constructor yang akan dijalankan otomatis saat objek Node dibuat.

self.key = key
Baris ini menyimpan nilai data ke dalam node.

self.left = None
Baris ini menginisialisasi child kiri dengan nilai kosong (None).

self.right = None
Baris ini menginisialisasi child kanan dengan nilai kosong (None).


<img width="572" height="255" alt="Screenshot 2026-05-24 121136" src="https://github.com/user-attachments/assets/ee9b93ea-d41a-4d7b-a92d-6c671998e06c" />

class BSTNilaiMahasiswa:
Baris ini membuat class utama Binary Search Tree untuk menyimpan data nilai mahasiswa.

def __init__(self):
Constructor pada class BST yang dijalankan saat objek BST dibuat.

self.root = None
Baris ini mengatur root awal BST menjadi kosong.

def insert_node(self, root, key):
Method ini digunakan untuk menambahkan node baru ke dalam BST secara rekursif.

if root is None:
Mengecek apakah posisi node masih kosong.

return Node(key)
Jika kosong, maka dibuat node baru berisi nilai yang dimasukkan.

if key < root.key:
Mengecek apakah nilai lebih kecil dari root.

root.left = self.insert_node(root.left, key)
Jika lebih kecil, data dimasukkan ke subtree kiri.

elif key > root.key:
Mengecek apakah nilai lebih besar dari root.

root.right = self.insert_node(root.right, key)
Jika lebih besar, data dimasukkan ke subtree kanan.

return root
Mengembalikan node root setelah proses insert selesai.

<img width="538" height="166" alt="Screenshot 2026-05-24 121155" src="https://github.com/user-attachments/assets/8b963b74-bb75-411b-9727-8fa23069c64b" />

def insert(self, key):
Method untuk memanggil proses insert dari luar class.

self.root = self.insert_node(self.root, key)
Menambahkan data mulai dari root utama BST.

def find_min_node(self, root):
Method untuk mencari node dengan nilai terkecil.

current = root
Variabel current digunakan untuk menelusuri node.

while current is not None and current.left is not None:
Perulangan berjalan selama masih ada child kiri.

current = current.left
Berpindah terus ke node paling kiri.

return current
Mengembalikan node dengan nilai terkecil.

<img width="589" height="594" alt="Screenshot 2026-05-24 121953" src="https://github.com/user-attachments/assets/1df41a1b-d985-487b-b727-508e9ca44a06" />

def delete_node(self, root, key):
Method untuk menghapus node dari BST.

if root is None:
Mengecek apakah tree kosong.

return None
Jika kosong maka tidak ada data yang dihapus.

if key < root.key:
Mengecek apakah nilai yang dicari lebih kecil dari root.

root.left = self.delete_node(root.left, key)
Pencarian dilanjutkan ke subtree kiri.

elif key > root.key:
Mengecek apakah nilai lebih besar dari root.

root.right = self.delete_node(root.right, key)
Pencarian dilanjutkan ke subtree kanan.

else:
Bagian ini dijalankan jika data ditemukan.

if root.left is None and root.right is None:
Mengecek apakah node tidak memiliki child.

return None
Node langsung dihapus.

elif root.left is None:
Mengecek apakah hanya memiliki child kanan.

return root.right
Node diganti dengan child kanan.

elif root.right is None:
Mengecek apakah hanya memiliki child kiri.

return root.left
Node diganti dengan child kiri.

else:
Bagian ini dijalankan jika node memiliki dua child.

successor = self.find_min_node(root.right)
Mencari successor dari subtree kanan.

root.key = successor.key
Mengganti nilai node dengan nilai successor.

root.right = self.delete_node(root.right, successor.key)
Menghapus node successor yang lama.

return root
Mengembalikan root setelah proses delete selesai.

def delete(self, key):
Method untuk memanggil proses delete dari luar class.

self.root = self.delete_node(self.root, key)
Menghapus data mulai dari root BST.

def height(self, root):
Method untuk menghitung tinggi pohon BST.

if root is None:
Mengecek apakah node kosong.

if root is None:
Mengecek apakah node kosong.

height_left = self.height(root.left)
Menghitung tinggi subtree kiri.

height_right = self.height(root.right)
Menghitung tinggi subtree kanan.

return 1 + max(height_left, height_right)
Mengambil tinggi terbesar lalu ditambah 1.

<img width="810" height="668" alt="Screenshot 2026-05-24 122008" src="https://github.com/user-attachments/assets/56724fbd-26ba-44f2-bac2-c95679443468" />

def level_order(self, root):
Method untuk menampilkan data dengan traversal level-order.

if root is None:
Mengecek apakah BST kosong.

print("(data nilai kosong)")
Menampilkan pesan jika data kosong.

return
Menghentikan method.

queue = []
Membuat queue kosong.

queue.append(root)
Menambahkan root ke queue.

while len(queue) > 0:
Perulangan berjalan selama queue masih berisi data.

current = queue.pop(0)
Mengambil data paling depan dari queue.

print(current.key, end=" ")
Menampilkan nilai node.

if current.left is not None:
Mengecek apakah ada child kiri.

queue.append(current.left)
Menambahkan child kiri ke queue.

if current.right is not None:
Mengecek apakah ada child kanan.

queue.append(current.right)
Menambahkan child kanan ke queue.

print()
Membuat pindah baris setelah traversal selesai.

def find_successor(self, root, key):
Method untuk mencari successor suatu nilai.

current = root
Variabel untuk traversal node.

successor = None
Variabel penyimpan successor.

while current is not None:
Perulangan pencarian node.

if key < current.key:
Jika nilai lebih kecil dari current.

successor = current
Current sementara menjadi successor.

current = current.left
Berpindah ke kiri.

elif key > current.key:
Jika nilai lebih besar dari current.

current = current.right
Berpindah ke kanan.

else:
Jika data ditemukan.

break
Menghentikan perulangan.

if current is None:
Mengecek apakah data tidak ditemukan.

return None, False
Mengembalikan status gagal.

if current.right is not None:
Mengecek apakah node punya subtree kanan.

successor = self.find_min_node(current.right)
Mencari nilai terkecil di subtree kanan.

if successor is None:
Mengecek apakah successor tidak ada.

return None, False
Mengembalikan status gagal.

return successor.key, True
Mengembalikan nilai successor dan status berhasil.

<img width="545" height="443" alt="Screenshot 2026-05-24 122020" src="https://github.com/user-attachments/assets/e16c4ae4-e2ac-4120-b36d-54ea9ad6f1b9" />

def find_predecessor(self, root, key):
Method untuk mencari predecessor suatu node.

current = root
Variabel traversal node.

predecessor = None
Variabel penyimpan predecessor.

while current is not None:
Perulangan pencarian data.

if key > current.key:
Jika nilai lebih besar dari current.

predecessor = current
Current sementara menjadi predecessor.

current = current.right
Berpindah ke kanan.

elif key < current.key:
Jika nilai lebih kecil dari current.

current = current.left
Berpindah ke kiri.

else:
Jika data ditemukan.

break
Menghentikan perulangan.

if current is None:
Mengecek apakah data tidak ditemukan.

return None, False
Mengembalikan status gagal.

if current.left is not None:
Mengecek apakah node punya subtree kiri.

temp = current.left
Masuk ke subtree kiri.

while temp.right is not None:
Mencari node paling kanan.

temp = temp.right
Berpindah ke kanan.

predecessor = temp
Node terakhir menjadi predecessor.

if predecessor is None:
Mengecek apakah predecessor tidak ada.

return None, False
Mengembalikan status gagal.

return predecessor.key, True
Mengembalikan nilai predecessor dan status berhasil.

<img width="449" height="277" alt="Screenshot 2026-05-24 123918" src="https://github.com/user-attachments/assets/92310a4e-e81f-4ed7-9f1b-efefa58b1ca4" />

def main():
Function utama program.

bst = BSTNilaiMahasiswa()
Membuat objek BST baru.

pilih = 0
Variabel untuk menyimpan pilihan menu.

while pilih != 7:
Perulangan program sampai user memilih keluar.

print("\n=== BST Data Nilai Mahasiswa ===")
Menampilkan judul program.

print("1. Tambah Nilai Mahasiswa")
Menampilkan menu tambah data.

print("2. Hapus Nilai Mahasiswa")
Menampilkan menu hapus data.

print("3. Tampilkan Data Nilai")
Menampilkan menu traversal data.

print("4. Lihat Tinggi Pohon")
Menampilkan menu tinggi pohon.

print("5. Cari Nilai Successor")
Menampilkan menu successor.

print("6. Cari Nilai Predecessor")
Menampilkan menu predecessor.

print("7. Keluar")
Menampilkan menu keluar.

<img width="935" height="775" alt="Screenshot 2026-05-24 123940" src="https://github.com/user-attachments/assets/9fb23aae-998f-42fa-9a69-9942f8ffe92a" />

try:
Digunakan untuk menangani error input.

pilih = int(input("Pilih menu: "))
Menerima input pilihan menu dari user.

except ValueError:
Menangkap error jika input bukan angka.

print("Input tidak valid!")
Menampilkan pesan error input.

continue
Mengulang menu kembali.

if pilih == 1:
Mengecek apakah user memilih menu tambah data.

x = int(input("Masukkan nilai mahasiswa: "))
Menerima input nilai mahasiswa.

bst.insert(x)
Menambahkan nilai ke BST.

print(f"Nilai mahasiswa {x} berhasil ditambahkan")
Menampilkan pesan berhasil.

elif pilih == 2:
Mengecek apakah user memilih hapus data.

x = int(input("Masukkan nilai yang akan dihapus: "))
Meminta input nilai yang akan dihapus.

bst.delete(x)
Menghapus nilai dari BST.

print(f"Nilai mahasiswa {x} berhasil dihapus")
Menampilkan pesan berhasil hapus.

elif pilih == 3:
Mengecek menu tampil data.

print("Daftar nilai mahasiswa: ", end="")
Menampilkan teks sebelum traversal.

bst.level_order(bst.root)
Menjalankan traversal level-order.

elif pilih == 4:
Mengecek menu tinggi pohon.

print(f"Tinggi pohon data nilai: {bst.height(bst.root)}")
Menampilkan tinggi BST.

elif pilih == 5:
Mengecek menu successor.

x = int(input("Cari successor dari nilai: "))
Meminta input nilai.

ans, found = bst.find_successor(bst.root, x)
Mencari successor nilai.

if found:
Mengecek apakah successor ditemukan.

print(f"Nilai setelah {x} adalah {ans}")
Menampilkan successor.

else:
Jika successor tidak ditemukan.

print("Tidak ada successor (nilai terbesar atau data tidak ditemukan)")
Menampilkan pesan gagal.

<img width="889" height="417" alt="Screenshot 2026-05-24 123957" src="https://github.com/user-attachments/assets/3a0d1538-189a-47f7-84f7-39f54caba2aa" />


elif pilih == 6:
Mengecek menu predecessor.

x = int(input("Cari predecessor dari nilai: "))
Meminta input nilai.

ans, found = bst.find_predecessor(bst.root, x)
Mencari predecessor nilai.

if found:
Mengecek apakah predecessor ditemukan.

print(f"Nilai sebelum {x} adalah {ans}")
Menampilkan predecessor.

else:
Jika predecessor tidak ditemukan.

print("Tidak ada predecessor (nilai terkecil atau data tidak ditemukan)")
Menampilkan pesan gagal.

elif pilih == 7:
Mengecek apakah user memilih keluar.

print("Program selesai.")
Menampilkan pesan program selesai.

else:
Dijalankan jika menu tidak tersedia.

print("Pilihan tidak valid!")
Menampilkan pesan pilihan salah.

if __name__ == "__main__":
Mengecek apakah file dijalankan langsung.

main()
Menjalankan function utama program.


**OUTPUR PROGRAM DAN PENJELASAN**

<img width="608" height="874" alt="Screenshot 2026-05-24 125618" src="https://github.com/user-attachments/assets/78f7a29b-6784-42c5-84d4-d1e9b45c5aa0" />
<img width="721" height="831" alt="Screenshot 2026-05-24 125636" src="https://github.com/user-attachments/assets/18ec2600-8eb4-478b-8aaf-0a2cf0097018" />
<img width="485" height="261" alt="Screenshot 2026-05-24 125646" src="https://github.com/user-attachments/assets/d397c5c2-14fb-4bdc-82e2-dbf12d0338b8" />

Pada awal program, ditampilkan menu utama yang berisi beberapa pilihan seperti menambah nilai mahasiswa,
menghapus nilai, menampilkan data, melihat tinggi pohon, mencari successor, mencari predecessor, dan keluar dari program.

Saat user memilih menu 1, program meminta input nilai mahasiswa. Nilai 70 dimasukkan dan berhasil ditambahkan ke dalam BST 
sehingga nilai tersebut menjadi root awal pohon. Setelah itu user kembali memilih menu 1 dan memasukkan nilai 80. 
Karena 80 lebih besar dari 70, maka data ditempatkan di sebelah kanan root. Selanjutnya nilai 90 juga ditambahkan, 
dan karena lebih besar dari 70 dan 80, maka ditempatkan di sebelah kanan node 80.

Ketika user memilih menu 2 untuk menghapus data dan memasukkan nilai 70, program berhasil menghapus node tersebut.
Karena 70 merupakan root dan memiliki child kanan, maka posisi root digantikan oleh node yang sesuai berdasarkan aturan BST.
Setelah penghapusan, data yang tersisa adalah 80 dan 90.

Pada menu 3, program menampilkan traversal level-order sehingga output yang muncul adalah 80 90.
Hal ini menunjukkan bahwa root pohon sekarang adalah 80 dan node 90 berada di sebelah kanan.

Saat memilih menu 4, program menampilkan tinggi pohon sebesar 1.
Nilai ini menunjukkan bahwa BST memiliki dua level, yaitu root 80 pada level 
pertama dan node 90 pada level kedua.

Pada menu 5, user mencari successor dari nilai 80. Output menunjukkan bahwa successor dari 80 adalah 90.
Hal ini karena 90 merupakan nilai terkecil yang lebih besar dari 80 pada BST.

Selanjutnya pada menu 6, user mencari predecessor dari nilai 90.
Output menunjukkan bahwa predecessor dari 90 adalah 80, karena 80 merupakan nilai terbesar yang lebih kecil dari 90.

Terakhir, saat user memilih menu 7, program menampilkan pesan “Program selesai.” 
yang menandakan bahwa proses eksekusi program telah berakhir.

Link Youtube : https://youtu.be/3m17QU_a2kA
              https://youtu.be/byTI4ZeXcD0
























