def menu():
    print("1. Tampilkan semua barang belanjaan")
    print("2. Tampilkan barang belanjaan beserta urutannya")
    print("3. Masukkan 5 daftar barang belanjaan")
    print("4. Ubah barang pada urutan tertentu")
    print("5. Keluar")

def main():
    belanjaan = [0] * 5
    running = True
    
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            print(f"Daftar Belanjaan saat ini: {belanjaan}") 
        elif choice == 2:
            for i in range(5):
                print(f"Barang ke-{i+1}: {belanjaan[i]}")  
        elif choice == 3:
            print("Masukkan 5 barang belanjaan:")
            for i in range(5):
                belanjaan[i] = input(f"Barang ke-{i+1} = ")
            print(f"Daftar belanjaan sekarang telah diperbarui: {belanjaan}") 
        elif choice == 4:
            try:
                idx = int(input("Masukkan urutan barang yang ingin diubah (1-5): "))
                if 1 <= idx <= 5:
                    barang_baru = input(f"Masukkan nama barang pengganti untuk urutan {idx}: ")
                    belanjaan[idx - 1] = barang_baru
                    print("Barang berhasil diperbarui.")
                else:
                    print("Urutan di luar jangkauan, masukkan angka 1 hingga 5.")
            except ValueError:
                print("Input urutan tidak valid, silakan masukkan angka!") 
        elif choice == 5:
            running = False
            print("selesai.")
        else:
            print("Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()