def print_odd_numbers(n):  # Membuat fungsi untuk mencetak bilangan ganjil hingga batas tertentu
    for i in range(1, n+1):  # Looping dari 1 hingga n (inklusif)
        if i % 2 != 0:  # Mengecek apakah nilai i adalah bilangan ganjil (hasil bagi 2 bukan 0)
            print(i, end=" ")  # Mencetak bilangan ganjil dengan spasi, tanpa membuat baris baru

n = int(input("Masukkan batas bilangan ganjil: "))  # Meminta input dari pengguna untuk batas angka
print_odd_numbers(n)  # Memanggil fungsi untuk mencetak bilangan ganjil hingga nilai n
