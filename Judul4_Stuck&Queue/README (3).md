**JUDUL : IMPLEMENTASI STACK ARRAY YAITU TUMPUKAN OMPRENG MBG**

**DESKRIPSI SINGKAT:**
Program ini merupakan penerapan struktur data **stack array** pada kasus **tumpukan ompreng** dengan konsep 
**LIFO (Last In First Out)**, yaitu ompreng yang terakhir dimasukkan akan menjadi yang pertama diambil.

Di dalam program terdapat beberapa operasi, seperti `push` untuk menambahkan ompreng ke tumpukan,
`pop` untuk mengambil ompreng paling atas, `peek` untuk melihat ompreng yang berada di posisi teratas,
serta `display` untuk menampilkan seluruh isi tumpukan dari atas ke bawah.
Program juga dilengkapi pengecekan kondisi saat tumpukan kosong atau penuh 
dan menyediakan menu interaktif untuk memudahkan pengguna dalam mengelola tumpukan ompreng.

**SOURCE KODE:**


<img width="519" height="148" alt="Screenshot 2026-05-17 125921" src="https://github.com/user-attachments/assets/e57c9f76-3f30-4d01-9dc7-0b33a1a34213" />

**Penjelasan**

class StackArray:
Baris ini digunakan untuk membuat kelas bernama StackArray yang berfungsi sebagai struktur data stack.

def __init__(self, max_size=100):
Method konstruktor yang dijalankan saat objek stack dibuat dengan kapasitas awal 100 data.

self.MAX = max_size
Digunakan untuk menyimpan kapasitas maksimum stack.

self.st = [None] * self.MAX
Membuat array kosong sebagai tempat penyimpanan data stack.

self.top_idx = -1
Menandakan bahwa stack masih kosong karena belum ada data.

<img width="836" height="754" alt="Screenshot 2026-05-17 125935" src="https://github.com/user-attachments/assets/0ce9da31-dc6e-4c26-873d-80ab7d47bd9c" />
<img width="768" height="262" alt="Screenshot 2026-05-17 125948" src="https://github.com/user-attachments/assets/c65a594a-d35e-4559-bdc4-498b032271e8" />

def is_empty(self):
Method untuk memeriksa apakah stack kosong.
return self.top_idx == -1
Menghasilkan nilai True jika stack kosong.

def is_full(self):
Method untuk memeriksa apakah stack penuh.
return self.top_idx == self.MAX - 1
Menghasilkan nilai True jika stack sudah mencapai kapasitas maksimum.

def push(self, x):
Method untuk menambahkan data ompreng ke dalam stack.
if self.is_full():
Memeriksa apakah stack penuh.
print("Tumpukan ompreng penuh")
Menampilkan pesan jika stack sudah penuh.
return
Menghentikan proses penambahan data.
self.top_idx += 1
Menambah posisi top satu tingkat ke atas.
self.st[self.top_idx] = x
Menyimpan data ompreng ke dalam stack.
print(f"Ompreng {x} berhasil ditambahkan")
Menampilkan pesan bahwa ompreng berhasil ditambahkan.

def pop(self):
Method untuk mengambil data paling atas dari stack.
if self.is_empty():
Memeriksa apakah stack kosong.
print("Tumpukan ompreng kosong")
Menampilkan pesan jika stack kosong.
return
Menghentikan proses pengambilan data.
print(f"Ompreng {self.st[self.top_idx]} berhasil diambil")
Menampilkan ompreng yang berhasil diambil.
self.top_idx -= 1
Mengurangi posisi top karena data teratas sudah dihapus.

def peek(self):
Method untuk melihat data paling atas tanpa menghapusnya.
if self.is_empty():
Memeriksa apakah stack kosong.
print("Tumpukan ompreng kosong")
Menampilkan pesan jika stack kosong.
return
Menghentikan proses.
print(f"Ompreng paling atas: {self.st[self.top_idx]}")
Menampilkan data ompreng yang berada di posisi paling atas.

def display(self):
Method untuk menampilkan seluruh isi stack.
if self.is_empty():
Memeriksa apakah stack kosong.
print("Tumpukan ompreng kosong")
Menampilkan pesan jika stack kosong.
return
Menghentikan proses.
print("Isi tumpukan ompreng (atas ke bawah): ", end="")
Menampilkan judul isi stack.
for i in range(self.top_idx, -1, -1):
Melakukan perulangan dari data paling atas ke paling bawah.
print(self.st[i], end=" ")
Menampilkan isi stack satu per satu.
print()
Membuat baris baru setelah seluruh data ditampilkan.

<img width="1099" height="811" alt="Screenshot 2026-05-17 130004" src="https://github.com/user-attachments/assets/261a3dea-6908-45b0-9540-c4108304520c" />

def main():
Fungsi utama program.
stack = StackArray()
Membuat objek stack dari kelas StackArray.
pilih = 0
Membuat variabel untuk menyimpan pilihan menu.

while pilih != 5:
Perulangan akan terus berjalan selama pengguna belum memilih keluar.

print("\n=== TUMPUKAN OMPRENG ===")
Menampilkan judul menu program.

print("1. Tambah Ompreng")
Menampilkan menu tambah ompreng.

print("2. Ambil Ompreng")
Menampilkan menu ambil ompreng.

print("3. Lihat Ompreng Teratas")
Menampilkan menu melihat ompreng teratas.

print("4. Tampilkan Tumpukan")
Menampilkan menu melihat seluruh isi stack.

print("5. Keluar")
Menampilkan menu keluar program.

try:
Digunakan untuk menangani kemungkinan kesalahan input.
pilih = int(input("Pilih: "))
Meminta pengguna memasukkan pilihan menu.
except ValueError:
Menangkap error jika input bukan angka.
print("Input tidak valid!")
Menampilkan pesan kesalahan input.
continue
Mengulang kembali ke menu utama.

if pilih == 1:
Memeriksa apakah pengguna memilih menu 1.
val = input("Masukkan kode ompreng: ")
Meminta input kode ompreng.
stack.push(val)
Menambahkan ompreng ke stack.

elif pilih == 2:
Memeriksa apakah pengguna memilih menu 2.
stack.pop()
Mengambil ompreng paling atas.

elif pilih == 3:
Memeriksa apakah pengguna memilih menu 3.
stack.peek()
Menampilkan ompreng paling atas.

elif pilih == 4:
Memeriksa apakah pengguna memilih menu 4.
stack.display()
Menampilkan seluruh isi tumpukan ompreng.

elif pilih == 5:
Memeriksa apakah pengguna memilih menu keluar.
print("Program selesai.")
Menampilkan pesan program selesai.

else:
Dijalankan jika pilihan menu tidak tersedia.
print("Pilihan tidak valid!")
Menampilkan pesan kesalahan pilihan menu.

<img width="346" height="73" alt="Screenshot 2026-05-17 130013" src="https://github.com/user-attachments/assets/5d3129cf-508b-4cb2-9418-73e54535c8d2" />
if __name__ == "__main__":
Memastikan program dijalankan secara langsung.
main()
Menjalankan fungsi utama program.

**OUTPUT PROGRAM**


<img width="903" height="708" alt="Screenshot 2026-05-17 132613" src="https://github.com/user-attachments/assets/53af3e7c-29f5-4b3c-a483-aedd44b68a5f" />

<img width="1042" height="462" alt="Screenshot 2026-05-17 132630" src="https://github.com/user-attachments/assets/3bc973e3-e6bc-431c-96bd-c2f7aa7d8cc7" />

Output program menampilkan beberapa pilihan menu untuk mengelola tumpukan ompreng,
seperti menambahkan ompreng, mengambil ompreng, melihat ompreng teratas, 
menampilkan seluruh isi tumpukan, dan keluar dari program. Saat pengguna menambahkan data, 
program akan memberikan notifikasi bahwa ompreng berhasil dimasukkan ke dalam stack. Ketika ompreng diambil,
program akan menampilkan data ompreng yang berada di posisi paling atas sesuai konsep LIFO. Selain itu,
program juga dapat menampilkan ompreng teratas dan seluruh isi tumpukan secara berurutan dari atas ke bawah.
Jika tumpukan kosong atau penuh, program akan memberikan pesan informasi sesuai kondisi tersebut.

Link Youtube:https://youtu.be/NHFAZXUSB34



















