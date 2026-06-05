**JUDUL : IMPLEMENTASI HASH MAP SEPARATE CHAINING TENTANG SISTEM NILAI MAHASISWA MENGGUNAKAN NPM**

**DESKRIPSI SINGKAT**
Hash Map Separate Chaining adalah salah satu metode implementasi hash map
yang digunakan untuk menyimpan data dalam bentuk pasangan key-value. Hash map 
bekerja dengan menggunakan fungsi hash untuk mengubah key menjadi indeks tertentu
pada hash table sehingga proses penyimpanan dan pencarian data dapat dilakukan dengan cepat.

Pada metode Separate Chaining, setiap indeks pada hash table dapat menyimpan
lebih dari satu data menggunakan struktur data linked list. Ketika dua atau lebih
key menghasilkan indeks yang sama (collision), data tidak ditimpa atau dipindahkan
ke indeks lain, melainkan disimpan dalam linked list pada indeks tersebut.
Dengan cara ini, seluruh data tetap dapat disimpan dan diakses dengan benar meskipun terjadi collision.

Metode Separate Chaining memiliki kelebihan dalam menangani collision 
secara sederhana dan fleksibel karena kapasitas penyimpanan pada setiap 
indeks dapat bertambah sesuai jumlah node dalam linked list. Operasi utama
yang dapat dilakukan pada hash map ini meliputi insert (menambah data),
search (mencari data), dan delete/remove (menghapus data). Oleh karena itu,
Hash Map Separate Chaining banyak digunakan pada sistem yang membutuhkan pencarian data yang cepat,
seperti sistem akademik, database, manajemen kontak, dan aplikasi berbasis pencarian data lainnya.

**SOURCE KODE DAN PENJELASAN**

<img width="313" height="105" alt="Screenshot 2026-06-05 210930" src="https://github.com/user-attachments/assets/ab957cb2-30e2-47c3-8ab9-6d6a63a5cc27" />

class Node:
Baris ini digunakan untuk mendefinisikan kelas Node. Kelas ini berfungsi sebagai struktur
data yang digunakan pada linked list untuk menyimpan pasangan key dan value dalam Hash Map.

def __init__(self, key, value):
Baris ini merupakan constructor dari kelas Node yang akan dijalankan secara otomatis ketika objek node baru dibuat.

self.key = key
Baris ini digunakan untuk menyimpan nilai key ke dalam atribut key milik objek. Pada kasus ini, key berisi NPM mahasiswa.

self.value = value
Baris ini digunakan untuk menyimpan nilai mahasiswa ke dalam atribut value.

self.next = None
Baris ini digunakan untuk menginisialisasi pointer next yang akan menunjuk ke node berikutnya.
Nilai awalnya None karena node belum terhubung dengan node lain.

<img width="349" height="93" alt="Screenshot 2026-06-05 210939" src="https://github.com/user-attachments/assets/57812743-8572-4004-b840-f4ed9e123850" />

class HashMapSeparateChaining:
Baris ini mendefinisikan kelas HashMapSeparateChaining yang digunakan sebagai 
implementasi Hash Map dengan metode Separate Chaining.

def __init__(self, size=10):
Baris ini merupakan constructor kelas Hash Map yang akan dijalankan saat objek Hash Map dibuat.

self.SIZE = size
Baris ini menyimpan ukuran hash table ke dalam atribut SIZE.

self.table = [None] * self.SIZE
Baris ini membuat list berukuran 10 elemen yang seluruhnya berisi None sebagai tempat penyimpanan data.

<img width="500" height="55" alt="Screenshot 2026-06-05 210947" src="https://github.com/user-attachments/assets/9532a936-d61b-4ecc-8c10-502f4794cb49" />

def hash_function(self, key):
Baris ini mendefinisikan fungsi hash yang digunakan untuk menghitung indeks penyimpanan data.

return (key % self.SIZE + self.SIZE) % self.SIZE
Baris ini menghitung indeks hash berdasarkan nilai key dan ukuran
tabel sehingga menghasilkan indeks antara 0 sampai 9.

<img width="405" height="236" alt="Screenshot 2026-06-05 210957" src="https://github.com/user-attachments/assets/66d3d2b5-5b39-49a0-b86f-4a2aa1525400" />

def insert(self, key, value):
Baris ini mendefinisikan fungsi untuk menambahkan data baru ke dalam Hash Map.

index = self.hash_function(key)
Baris ini menghitung indeks tempat data akan disimpan menggunakan fungsi hash.

current = self.table[index]
Baris ini mengambil node pertama yang berada pada indeks tersebut.

while current is not None:
Baris ini melakukan perulangan selama masih terdapat node pada linked list.

if current.key == key:
Baris ini memeriksa apakah key yang sedang dicari sudah ada dalam linked list.

current.value = value
Baris ini memperbarui nilai apabila key yang sama ditemukan.

return
Baris ini menghentikan fungsi setelah proses pembaruan selesai.

current = current.next
Baris ini memindahkan pemeriksaan ke node berikutnya dalam linked list.

new_node = Node(key, value)
Baris ini membuat node baru yang berisi key dan value.

new_node.next = self.table[index]
Baris ini menghubungkan node baru dengan node lama yang sudah ada pada indeks tersebut.


<img width="381" height="166" alt="Screenshot 2026-06-05 211008" src="https://github.com/user-attachments/assets/f43a8a12-d3dc-401e-a088-d4b8fe75d811" />

def search(self, key):
Baris ini mendefinisikan fungsi untuk mencari data berdasarkan key.

index = self.hash_function(key)
Baris ini menghitung indeks berdasarkan key yang dicari.

current = self.table[index]
Baris ini mengambil node pertama pada indeks tersebut.

while current is not None:
Baris ini melakukan penelusuran linked list.

if current.key == key:
Baris ini memeriksa apakah key pada node saat ini sama dengan key yang dicari.

return current
Baris ini mengembalikan node jika data ditemukan.

current = current.next
Baris ini berpindah ke node berikutnya jika data belum ditemukan.

return None
Baris ini mengembalikan nilai None jika data tidak ditemukan.


<img width="525" height="282" alt="Screenshot 2026-06-05 211019" src="https://github.com/user-attachments/assets/65a626bb-f3ed-4bf5-ba95-b4866d5ead06" />

def remove_key(self, key):
Baris ini mendefinisikan fungsi untuk menghapus data berdasarkan key.

index = self.hash_function(key)
Baris ini menghitung indeks tempat data berada.

current = self.table[index]
Baris ini mengambil node pertama pada indeks tersebut.

prev = None
Baris ini digunakan untuk menyimpan node sebelumnya selama proses penelusuran.

while current is not None:
Baris ini melakukan perulangan selama masih ada node yang diperiksa.

if current.key == key:
Baris ini memeriksa apakah key yang dicari ditemukan.

if prev is None:
Baris ini memeriksa apakah node yang ditemukan berada di awal linked list.

self.table[index] = current.next
Baris ini menghapus node pertama dengan menggantinya menggunakan node berikutnya.

else:
Baris ini dijalankan jika node yang dihapus bukan node pertama.

prev.next = current.next
Baris ini menghubungkan node sebelumnya langsung ke node setelah node yang dihapus.

return True
Baris ini mengembalikan nilai True sebagai tanda bahwa penghapusan berhasil.

prev = current
Baris ini menyimpan node saat ini sebagai node sebelumnya.

current = current.next
Baris ini berpindah ke node berikutnya.

return False
Baris ini mengembalikan nilai False jika key tidak ditemukan.


<img width="612" height="225" alt="Screenshot 2026-06-05 211026" src="https://github.com/user-attachments/assets/e247a84a-7598-48c1-8c09-36cb85147e24" />

def display(self):
Baris ini mendefinisikan fungsi untuk menampilkan isi Hash Map.

print("\nIsi Hash Table (Separate Chaining):")
Baris ini menampilkan judul output.

for i in range(self.SIZE):
Baris ini melakukan perulangan dari indeks 0 sampai indeks 9.

print(f"{i}: ", end="")
Baris ini menampilkan nomor indeks hash table.

current = self.table[i]
Baris ini mengambil node pertama pada indeks yang sedang ditampilkan.

while current is not None:
Baris ini menelusuri linked list pada indeks tersebut.

print(f"({current.key},{current.value}) -> ", end="")
Baris ini menampilkan key dan value dari node saat ini.

current = current.next
Baris ini berpindah ke node berikutnya.

print("NULL")
Baris ini menandakan bahwa tidak ada lagi node setelah node terakhir.


<img width="647" height="419" alt="Screenshot 2026-06-05 211034" src="https://github.com/user-attachments/assets/25e192cd-fb70-4d82-8d97-a9282467aba8" />

def main():
Baris ini mendefinisikan fungsi utama program.

hashmap = HashMapSeparateChaining()
Baris ini membuat objek Hash Map baru.

hashmap.insert(2515061019, 85)
Baris ini menambahkan data mahasiswa dengan NPM 2515061019 dan nilai 85.

hashmap.insert(2515061020, 90)
Baris ini menambahkan data mahasiswa dengan NPM 2515061020 dan nilai 90.

hashmap.insert(2515061021, 78)
Baris ini menambahkan data mahasiswa dengan NPM 2515061021 dan nilai 78.

hashmap.insert(2515061022, 88)
Baris ini menambahkan data mahasiswa dengan NPM 2515061022 dan nilai 88.

hashmap.display()
Baris ini menampilkan seluruh data yang tersimpan dalam hash table.

hasil = hashmap.search(2515061020)
Baris ini mencari data mahasiswa dengan NPM 2515061020.

if hasil is not None:
Baris ini memeriksa apakah data berhasil ditemukan.

print(f"\nNPM 2515061020 ditemukan dengan nilai = {hasil.value}")
Baris ini menampilkan nilai mahasiswa jika data ditemukan.

else:
Baris ini dijalankan jika data tidak ditemukan.

print("\nNPM 2515061020 tidak ditemukan")
Baris ini menampilkan pesan bahwa data tidak ditemukan.

hashmap.remove_key(2515061020)
Baris ini menghapus data mahasiswa dengan NPM 2515061020.

print("\nSetelah menghapus data mahasiswa dengan NPM 2515061020:")
Baris ini menampilkan informasi bahwa proses penghapusan telah dilakukan.

hashmap.display()
Baris ini menampilkan kembali isi hash table setelah data dihapus.

if __name__ == "__main__":
Baris ini memastikan bahwa fungsi main() hanya dijalankan ketika file Python dieksekusi secara langsung.

main()
Baris ini memanggil fungsi utama sehingga seluruh program dapat dijalankan.

**OUTPUT**


<img width="582" height="511" alt="Screenshot 2026-06-05 215351" src="https://github.com/user-attachments/assets/f9d184b0-ff7a-4a59-b2c4-1404713906f9" />

### Penjelasan Output

Output pertama menampilkan isi hash table setelah data mahasiswa dimasukkan.
Setiap NPM disimpan pada indeks yang diperoleh dari hasil fungsi hash (`NPM % 10`).
Data mahasiswa dengan NPM 2515061020, 2515061021, 2515061022, dan 2515061019 berhasil
tersimpan pada indeks 0, 1, 2, dan 9, sedangkan indeks lainnya masih kosong (`NULL`).



Selanjutnya, program melakukan pencarian data mahasiswa dengan NPM 2515061020.
Karena data ditemukan dalam hash table, program menampilkan informasi bahwa mahasiswa 
tersebut memiliki nilai 90.



Setelah itu, program menghapus data mahasiswa dengan NPM 2515061020. 
Hasil tampilan hash table setelah penghapusan menunjukkan bahwa indeks 0 
menjadi kosong (`NULL`), sementara data mahasiswa lainnya tetap tersimpan.
Hal ini membuktikan bahwa operasi **insert**, **search**, dan **remove** pada 
Hash Map Separate Chaining berhasil dijalankan dengan baik.

Link Youtube:https://youtu.be/QK2eayh6nuo






















