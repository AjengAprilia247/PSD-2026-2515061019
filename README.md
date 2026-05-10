*JUDUL : MENGIMPLEMENTASIKAN PENCARIAN MENGGUNAKAN 
SEQUENTIAL SEARCH DALAM PENCARIAN DATA BUMBU*

*DESKRIPSI SINGKAT*
implementasi searching menerapkan metode Sequential Search untuk mencari 
nama bumbu masakan pada sebuah array. Pengguna diminta memasukkan bumbu yang ingin dicari,
lalu program akan memeriksa data satu per satu secara berurutan mulai dari awal hingga akhir array. 
Apabila bumbu ditemukan, program akan menampilkan jumlah kemunculannya, 
sedangkan jika tidak ditemukan maka akan muncul pesan bahwa bumbu tersebut tidak ada dalam data.

SOURCE CODE


<img width="527" height="255" alt="Screenshot 2026-05-09 102045" src="https://github.com/user-attachments/assets/7dab0bee-6251-4b9a-aff8-7bcde40bf13c" />

PENJELASAN 

Fungsi def sequential_search(data, n, target): digunakan untuk membuat fungsi pencarian sequential search.
Fungsi ini menerima tiga parameter, yaitu data sebagai kumpulan data bumbu masakan,
n sebagai jumlah data dalam array, dan target sebagai bumbu yang ingin dicari

Baris i = 0 digunakan untuk membuat variabel indeks dengan nilai awal 0.
Variabel ini berfungsi sebagai penunjuk posisi data yang sedang diperiksa dalam array.

Baris counter = 0 digunakan untuk membuat variabel penghitung jumlah data yang ditemukan.
Nilai awal dibuat 0 karena belum ada data yang cocok saat program mulai dijalankan.

Baris while i < n: merupakan perulangan yang berjalan selama nilai i masih lebih kecil dari jumlah data. 
Perulangan ini digunakan untuk memeriksa seluruh data bumbu secara berurutan dari awal hingga akhir array.

Baris if data[i] == target: digunakan untuk mengecek apakah data pada indeks ke-i
sama dengan nilai target yang dimasukkan pengguna.

Baris counter += 1 digunakan untuk menambahkan nilai variabel counter sebanyak 1 
ketika data yang dicari berhasil ditemukan dalam array.

Baris i += 1 digunakan untuk menambah nilai indeks agar proses pencarian berpindah ke data berikutnya.

Baris return counter digunakan untuk mengembalikan nilai counter sebagai hasil akhir berupa 
jumlah kemunculan data yang ditemukan.

<img width="857" height="580" alt="image" src="https://github.com/user-attachments/assets/26423b2d-5d5c-4af3-89ce-b7ef2d5e7962" />

PENJELASAN :

Fungsi def main(): berfungsi sebagai fungsi utama yang menjalankan seluruh proses
program pencarian data.

Baris data = ["garam", "gula", "lada", "cabai", "garam", "jahe"] 
digunakan untuk membuat array yang berisi beberapa data bumbu masakan.

Baris n = len(data) digunakan untuk menghitung jumlah 
seluruh elemen dalam array menggunakan fungsi len(), kemudian 
hasilnya disimpan ke variabel n.

Baris print(f"Data array: {data}") digunakan untuk menampilkan seluruh isi data array ke layar.

Baris while True: digunakan untuk membuat perulangan terus-menerus
hingga pengguna berhasil memberikan input yang benar.

Baris try: digunakan untuk mencoba menjalankan kode yang berpotensi menimbulkan kesalahan saat program dijalankan.

Baris target = input("Masukkan bumbu yang ingin dicari: ") digunakan untuk meminta pengguna 
memasukkan nama bumbu yang akan dicari dalam array.

Baris break digunakan untuk menghentikan perulangan apabila input berhasil dimasukkan.

Baris except ValueError:
digunakan untuk menangani kesalahan input jika terjadi error pada program.

Baris print("Input tidak valid, silakan masukkan bumbu!") digunakan untuk menampilkan
pesan kesalahan apabila input yang diberikan tidak sesuai.

Baris counter = sequential_search(data, n, target) digunakan untuk memanggil

fungsi sequential_search guna mencari jumlah kemunculan bumbu yang dimasukkan pengguna.

Baris if counter > 0: digunakan untuk memeriksa apakah
bumbu yang dicari berhasil ditemukan di dalam array.

Baris print(f"Bumbu {target} ditemukan sebanyak {counter} kali.")
digunakan untuk menampilkan informasi bahwa bumbu berhasil ditemukan beserta jumlah kemunculannya.

Baris else: dijalankan apabila data bumbu yang dicari tidak ditemukan dalam array.

Baris print(f"Bumbu {target} tidak ditemukan.") 
digunakan untuk menampilkan pesan bahwa bumbu yang dicari tidak tersedia pada data.

Baris if __name__ == "__main__": digunakan untuk memastikan bahwa
program dijalankan secara langsung, bukan dipanggil dari file Python lain.

Baris main() digunakan untuk memanggil fungsi utama agar seluruh program dapat dieksekusi.

OUTPUT:

<img width="1365" height="334" alt="Screenshot 2026-05-09 104112" src="https://github.com/user-attachments/assets/b881ffbf-a390-4548-b081-e881bcf52cd5" />

Hasil output program memperlihatkan data array yang berisi beberapa nama bumbu masakan, yaitu ['garam', 'cabai', 'gula', 'lada', 'cabai', 'garam', 'jahe']. 
Setelah itu, program meminta pengguna memasukkan nama bumbu yang ingin dicari, dan pada contoh tersebut pengguna memasukkan cabai. Program kemudian menjalankan 
proses pencarian dengan metode Sequential Search dengan memeriksa setiap data secara berurutan dari awal hingga akhir array.
Dari proses tersebut, program menemukan bahwa bumbu cabai muncul sebanyak 2 kali sehingga program menampilkan pesan Bumbu cabai ditemukan sebanyak 2 kali.
sebagai hasil pencarian.

Link youtube: https://youtu.be/KevmqRsbl24?si=wr0KUR934S5D78YA

