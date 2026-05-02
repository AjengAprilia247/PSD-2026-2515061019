**MENGIMPLEMENTASIKAN JUDUL 2 SORTING ,
MENGURUTKAN NAMA DALAM ABSEN DARI YANG TERPENDEK KE TERPANJANG
MENGGUNAKAN METODE BUBBLE SORT**

**DESKRIPSI SINGKAT**
Program ini adalah sebuah implementasi sederhana yang mengurutkan daftar nama berdasarkan panjang hurufnya
dengan metode **Bubble Sort**. Dimulai dengan meminta pengguna memasukkan jumlah data,
atau banyaknya nama yang ingin dimasukkan. Kemudian, pengguna diminta memasukkan nama satu per satu
hingga jumlah yang ditentukan terpenuhi.
Setelah semua data dimasukkan, program akan menampilkan daftar nama sebelum diurutkan. Kemudian,
proses pengurutan dilakukan dengan membandingkan panjang nama yang berdekatan, mengubahnya jika urutan tidak sesuai.
Proses ini dilakukan berulang kali hingga seluruh data tersusun rapi
dari nama yang paling pendek hingga yang paling panjang.
setelah itu, program menghasilkan daftar nama yang sudah terurut.
Program ini secara keseluruhan bertujuan untuk menunjukkan cara algoritma Bubble Sort 
mengurutkan data teks secara bertahap berdasarkan jumlah karakter hingga menghasilkan urutan yang tepat.


**SOURCE KODE:**
<img width="749" height="305" alt="Screenshot 2026-05-02 201245" src="https://github.com/user-attachments/assets/5027a11b-8490-4107-92ee-4f3bdae59a4c" />

<img width="795" height="749" alt="Screenshot 2026-05-02 201301" src="https://github.com/user-attachments/assets/22673b30-86c4-4d08-8149-63e5ac65c795" />




**PENJELASAN KODE**
<img width="326" height="130" alt="Screenshot 2026-05-02 202333" src="https://github.com/user-attachments/assets/7f24e7de-76a5-4f4b-b759-a46bac93c471" />
Pada baris pertama, def tukar(arr, i, j): mendefinisikan fungsi tukar dengan tiga parameter
arr adalah tempat penyimpanan data (list), dan i dan j adalah indeks elemen yang akan ditukar posisinya.

Pada baris kedua, Nilai elemen pada indeks i disimpan ke dalam variabel sementara temp, 
temp = arr[i], agar nilai tidak hilang selama proses penukaran.

Pada baris ketiga, Nilai pada indeks i ditukar dengan nilai pada indeks j, arr[i] = arr[j],
sehingga nilai yang ada di posisi i sekarang adalah nilai yang ada di posisi j sebelumnya.

dibaris keempat, arr[j] = temp dimasukkan ke dalam indeks j,
yang merupakan nilai yang telah disimpan di temp, atau nilai awal dari indeks i. 
Dengan demikian, proses pertukaran kedua elemen selesai.

<img width="582" height="176" alt="Screenshot 2026-05-02 203252" src="https://github.com/user-attachments/assets/d77a486c-3826-4cce-b5b2-c9374c993dc7" />
Baris pertama berisi deklarasi fungsi bubble_sort (def bubble_sort(arr, n).
Fungsi ini menerima dua parameter: arr adalah list data dan n adalah jumlah elemen dalam list tersebut.


pada baris kedua, for i in range(n - 1):, mengatur jumlah kali proses pengurutan dilakukan.
Karena satu elemen sudah berada di posisi yang tepat pada setiap iterasi, perulangan ini berjalan sebanyak n-1 kali.

pada baris ketiga, Untuk j dalam range(n - i - 1):, perulangan
digunakan untuk membandingkan elemen satu dengan elemen lain.
Karena bagian akhir array secara bertahap sudah terurut, batas perulangan dikurangi dengan i.

Baris keempat memiliki kondisi if len(arr[j]) > len(arr[j + 1], yang memungkinkan
perbandingan panjang karakter dua elemen yang berdekatan. 
Agar urutan benar, elemen di indeks j harus diganti jika panjangnya lebih besar daripada indeks j+1.

pada baris kelima, Jika kondisi terpenuhi, fungsi tukar (arr, j, j + 1) akan digunakan untuk mengubah posisi kedua. 
Setelah dilakukan berulang kali, seluruh data diurutkan menurut panjangnya.

<img width="782" height="632" alt="Screenshot 2026-05-02 204223" src="https://github.com/user-attachments/assets/6822ea28-0dd2-46ef-9843-e776419fafee" />
Baris def main(): mendefinisikan fungsi inti yang akan menjalankan seluruh proses program.

Baris try: digunakan untuk mengantisipasi kesalahan saat pengguna memasukkan data.

Baris n = int(input("Masukkan jumlah absen: "))
berfungsi untuk meminta pengguna memasukkan jumlah data, lalu mengubahnya menjadi tipe bilangan bulat.

Baris except ValueError:
akan dijalankan jika input yang diberikan tidak sesuai, misalnya bukan angka.

Baris print("Input tidak valid!") menampilkan pesan bahwa input yang dimasukkan salah.

Baris return digunakan untuk menghentikan eksekusi fungsi ketika terjadi kesalahan.

Baris arr = [] berfungsi membuat list kosong yang akan digunakan untuk menyimpan data yang dimasukkan.

Baris print("Masukkan nama absen:") memberikan instruksi kepada pengguna untuk mulai menginput data nama.

Baris for i in range(n): merupakan perulangan yang berjalan sebanyak jumlah data yang telah ditentukan.

Baris while True: digunakan untuk melakukan pengulangan terus-menerus sampai input yang diberikan benar.

Baris try: di dalam perulangan berfungsi untuk mengantisipasi kesalahan saat pengguna memasukkan data.

Baris nilai = input() digunakan untuk menerima data berupa nama dari pengguna.

Baris arr.append(nilai) berfungsi untuk menambahkan data yang telah dimasukkan ke dalam list.

Baris break digunakan untuk keluar dari perulangan jika input berhasil diproses.

Baris except ValueError: menangani kesalahan yang terjadi saat input dalam perulangan

Baris print("Input tidak valid, silakan masukkan nama!") menampilkan
pesan kesalahan agar pengguna mengulang input.

Baris print(f"Array sebelum diurutkan: {arr}") digunakan 
untuk menampilkan isi data sebelum dilakukan proses pengurutan.

Baris bubble_sort(arr, n) berfungsi memanggil proses pengurutan menggunakan metode Bubble Sort.

Baris print("Array setelah diurutkan (Bubble Sort):", end=" ")
menampilkan teks tanpa berpindah ke baris berikutnya.

Baris for i in range(n): digunakan untuk mengulang proses penampilan data yang sudah diurutkan.

Baris print(arr[i], end=" ") menampilkan setiap elemen dalam satu baris secara berurutan.

Baris print() digunakan untuk membuat baris baru setelah seluruh data selesai ditampilkan.

<img width="371" height="68" alt="Screenshot 2026-05-02 205343" src="https://github.com/user-attachments/assets/e8938cdc-3960-4dcd-ad87-855136b7984e" />
Baris if __name__ == "__main__" digunakan untuk menjamin bahwa 
kode yang terkandung di dalamnya hanya dijalankan saat file Python dijalankan secara langsung,
bukan saat diimpor sebagai modul ke dalam file lain.

Baris main() memanggil fungsi main, yang memungkinkan seluruh program yang telah dibuat di dalamnya dijalankan.


**OUTPUT**
<img width="756" height="224" alt="Screenshot 2026-05-02 205653" src="https://github.com/user-attachments/assets/082bc5ea-66ee-4305-b12c-798d8140fb9e" />
**penjelasan:**
Pada bagian Masukkan jumlah absen: 4, program meminta jumlah data yang akan dimasukkan,
dan pengguna mengisi angka 4, artinya akan ada empat nama yang diinput.
Selanjutnya, pada bagian Masukkan nama absen:, program meminta pengguna memasukkan nama satu per satu, yaitu
zia, nathania, ajeng, dan muhammad, yang kemudian disimpan ke dalam list.

Baris Array sebelum diurutkan: ['zia', 'nathania', 'ajeng', 'muhammad'] 
menampilkan isi list sesuai urutan saat pertama kali dimasukkan, sehingga urutannya 
masih sama seperti input awal pengguna.

Setelah itu, program melakukan proses pengurutan menggunakan metode Bubble Sort 
berdasarkan panjang karakter setiap nama. Hasilnya ditampilkan pada baris Array setelah diurutkan 
(Bubble Sort): zia ajeng nathania muhammad, di mana urutan berubah menjadi dari nama dengan 
jumlah huruf paling sedikit ke yang paling banyak. zia (3 huruf) berada di awal, diikuti ajeng (5 huruf),
kemudian nathania (8 huruf), dan terakhir muhammad (8 huruf).

Link Youtube:https://youtu.be/bQpFSHlBCcg







