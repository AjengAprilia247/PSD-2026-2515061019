def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ["garam","cabai", "gula", "lada", "cabai", "garam", "jahe"]
    n = len(data)
    print(f"Data array: {data}")
    while True:
        try:
            target = input("Masukkan nama bumbu yang ingin dicari: ")
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan nama bumbu!")
    counter = sequential_search(data, n, target)
    if counter > 0:
        print(f"Bumbu {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Bumbu {target} tidak ditemukan.")


if __name__ == "__main__":
    main()