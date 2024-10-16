def print_pattern(n):  # Membuat fungsi untuk mencetak pola angka berdasarkan nilai n
    for i in range(1, n+1):  # Looping dari 1 hingga n (inklusif)
        print(f"{i} " * i)  # Mencetak angka i sebanyak i kali di baris yang sama

# Meminta input dari pengguna untuk nilai n
n = int(input("Masukkan nilai n: "))

# Memanggil fungsi untuk mencetak pola angka berdasarkan nilai n
print_pattern(n)
