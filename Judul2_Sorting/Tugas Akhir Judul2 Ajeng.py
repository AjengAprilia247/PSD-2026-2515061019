def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah absen: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan nama absen:")
    for i in range(n):
        while True:
            try:
                nilai = input()
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan nama!")
    print(f"Array sebelum diurutkan: {arr}")
    bubble_sort(arr, n)
    print("Array setelah diurutkan (Bubble Sort):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    main()