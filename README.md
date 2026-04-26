program daftar belanjaan menggunakan list 1 dimensi

Program ini adalah implementasi sederhana dari struktur data list 1 dimensi dalam Python.
Digunakan untuk mencatat dan mengelola daftar belanjaan dengan kapasitas tetap sebanyak lima item.

Menu interaktif berbasis terminal memungkinkan pengguna dapat melihat, mengisi, dan mengubah daftar belanjaan.
Karena program menggunakan list dengan ukuran tetap (5 data), jumlah barang yang dapat dimasukkan juga terbatas pada 5 item.
Data barang belanjaan akan disimpan sesuai urutan index dalam list jika pengguna menambahkan data.

code:

<img width="718" height="175" alt="Screenshot 2026-04-26 112051" src="https://github.com/user-attachments/assets/59891229-c9b0-4a50-856e-033e299d3d5a" />
Dalam kode tersebut, fungsi menu() berfungsi untuk menampilkan daftar opsi yang tersedia dalam program daftar belanjaan.
Fungsi ini memiliki lima perintah print(), yang masing-masing menampilkan pilihan yang dapat dipilih oleh pengguna
contohnya, mereka dapat menampilkan semua barang belanjaan, menampilkan barang beserta urutannya,
memasukkan lima daftar barang belanjaan, mengubah barang pada urutan tertentu, dan keluar dari program. 
Dengan menggunakan fungsi ini, pengguna dapat melihat semua barang belanja



<img width="301" height="70" alt="Screenshot 2026-04-26 112612" src="https://github.com/user-attachments/assets/405ba153-608a-4fbe-a030-1315e4a14686" />

dalam bagian kode def main():. Fungsi tersebut memulai variabel belanjaan dengan nilai [0] * 5, 
yang menunjukkan bahwa program membuat sebuah list dengan lima elemen, masing-masing dengan nilai awal 0. 
List ini digunakan untuk menyimpan data barang belanjaan yang akan dimasukkan oleh pengguna. 
Penggunaan ukuran tetap lima elemen menunjukkan bahwa program membatasi jumlah data yang dapat disimpan, 
sehingga hanya lima barang yang dapat dimasukkan ke dalam daftar belanjaan.



<img width="538" height="231" alt="Screenshot 2026-04-26 112637" src="https://github.com/user-attachments/assets/42f499b8-a504-4d46-bd42-523732194887" />
Pada bagian kode ini, variabel running diinisialisasi dengan nilai True,
yang berfungsi sebagai penanda bahwa program terus berjalan. Kemudian digunakan perulangan while running, 
yang membuat program menampilkan menu secara berulang selama nilai running masih True.
Dalam perulangan ini, fungsi menu() dipanggil untuk menampilkan pilihan kepada pengguna, dan program kemudian meminta input,
yang berupa angka yang disimpan ke dalam variabel pilihan.
Proses input ini dibungkus dengan try-except untuk menangani kesalahan jika pengguna memasukkan data yang bukan angka. 
Jika terjadi kesalahan value, program akan menampilkan pesan peringatan dan mengulangi proses input tanpa menghentikan program.

<img width="637" height="68" alt="Screenshot 2026-04-26 112702" src="https://github.com/user-attachments/assets/4df13a20-4c0d-437b-83c5-c3d3a8351487" />
Kode tersebut mengecek apakah pengguna memilih opsi 1, dan jika iya, program akan menampilkan daftar belanja yang tersimpan dalam variabel belanjaan.

<img width="591" height="95" alt="Screenshot 2026-04-26 112750" src="https://github.com/user-attachments/assets/a414bb3f-d78e-44cc-82e3-ab1f24c3a7a6" />
Kode ini digunakan ketika pengguna memilih opsi 2, 
yang akan memungkinkan program untuk menampilkan daftar belanja satu per satu menggunakan perulangan for.
Fungsi range(5) membatasi perulangan sebanyak lima kali, dan setiap item ditampilkan dengan nomor urut (i+1),
bersama dengan konten dari daftar belanjaan.

<img width="829" height="145" alt="Screenshot 2026-04-26 112802" src="https://github.com/user-attachments/assets/03b4b33d-9090-451a-ba71-aee408a4d77c" />
Kode ini diaktifkan saat pengguna memilih opsi 3, yang memungkinkan untuk memperbarui daftar belanja. 
Program akan meminta pengguna memasukkan lima barang secara berurutan, lalu menyimpannya ke dalam list belanjaan.
Setelah selesai, daftar belanja yang telah diperbarui akan ditampilkan kembali.

<img width="1043" height="356" alt="Screenshot 2026-04-26 112819" src="https://github.com/user-attachments/assets/6289ee05-81b2-4da7-a946-00e37c26ed18" />
Kode ini digunakan untuk mengubah satu barang tertentu dalam daftar belanja. Pengguna diminta memasukkan nomor urutan barang (1–5), 
lalu menggantinya dengan barang baru; program juga menangani kesalahan input jika angka tidak valid atau di luar jangkauan.

<img width="628" height="283" alt="Screenshot 2026-04-26 112830" src="https://github.com/user-attachments/assets/2371ce05-df15-4cea-b5e6-3ebafa5189e6" />
Saat pengguna memilih opsi 5, kode ini digunakan untuk menghentikan program dengan mengubah status running menjadi False.
Ini juga menampilkan pesan bahwa program selesai. Jika input tidak sesuai dengan pilihan yang tersedia,
program akan menampilkan pesan bahwa pilihan tersebut tidak valid. Bagian if __name__ == "__main__" menjamin 
bahwa fungsi main() akan digunakan saat file dieksekusi langsung.









output dari program:


pilihan 1:
<img width="555" height="185" alt="Screenshot 2026-04-26 120343" src="https://github.com/user-attachments/assets/9309b258-02c1-4c43-aee1-c86af9b23eff" />

pilihan 2:
<img width="572" height="315" alt="Screenshot 2026-04-26 120415" src="https://github.com/user-attachments/assets/47c73cc9-5c33-4db3-ad9b-a17002119452" />

pilihan 3:
<img width="1044" height="366" alt="Screenshot 2026-04-26 120453" src="https://github.com/user-attachments/assets/4087ed87-ef53-4c57-bf43-e18090b50612" />

pilihan 4:
<img width="848" height="414" alt="Screenshot 2026-04-26 120543" src="https://github.com/user-attachments/assets/a9c1eabe-1ded-42c0-be24-7e45fe5e0492" />

pilihan 5:
<img width="223" height="56" alt="Screenshot 2026-04-26 120604" src="https://github.com/user-attachments/assets/965a909d-9efb-40d2-90ef-beed3e2b658a" />

Output program diawali dengan menampilkan menu pilihan (1–5) secara berulang.
Setiap kali pengguna memasukkan angka, program akan memberikan output sesuai pilihan tersebut. 
Jika memilih opsi 1, program menampilkan seluruh isi daftar belanja dalam bentuk list.
Opsi 2 menampilkan setiap barang satu per satu lengkap dengan nomor urutnya. 
Opsi 3 meminta pengguna memasukkan 5 barang, lalu menampilkan daftar yang sudah diperbarui.
Opsi 4 memungkinkan pengguna mengubah satu barang tertentu berdasarkan nomor urutan,
kemudian menampilkan pesan bahwa perubahan berhasil atau error jika input tidak valid.
Jika pengguna memasukkan input yang bukan angka atau di luar pilihan, program akan menampilkan pesan kesalahan. 
Program akan terus menampilkan menu hingga pengguna memilih opsi 5, 
yang kemudian menampilkan pesan bahwa program selesai dan berhenti berjalan.


link youtube:https://youtu.be/mrltBeDl21o



