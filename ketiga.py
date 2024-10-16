def fibonacci(n):  # Membuat fungsi untuk menghasilkan deret Fibonacci dengan n elemen
    fib = [0, 1]  # Inisialisasi list dengan dua angka pertama dalam deret Fibonacci
    while len(fib) < n:  # Melakukan looping sampai panjang list fib mencapai n
        fib.append(fib[-1] + fib[-2])  # Menambahkan elemen baru, yaitu jumlah dari dua elemen terakhir
    return fib[:n]  # Mengembalikan list Fibonacci dengan n elemen pertama

# Meminta input dari pengguna untuk jumlah angka dalam deret Fibonacci
n = int(input("Masukkan jumlah angka Fibonacci yang diinginkan: "))

# Memanggil fungsi fibonacci untuk menghasilkan deret dengan n elemen
result = fibonacci(n)

# Mencetak hasil deret Fibonacci
print(f"Deret Fibonacci hingga {n} angka: {result}")
