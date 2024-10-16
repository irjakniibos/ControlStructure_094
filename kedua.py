def find_largest(a, b, c):  # Membuat fungsi untuk mencari bilangan terbesar dari tiga input
    if a >= b and a >= c:  # Mengecek apakah a lebih besar atau sama dengan b dan c
        return a  # Jika benar, kembalikan nilai a sebagai yang terbesar
    elif b >= a and b >= c:  # Mengecek apakah b lebih besar atau sama dengan a dan c
        return b  # Jika benar, kembalikan nilai b sebagai yang terbesar
    else:  # Jika kedua kondisi di atas salah, berarti c adalah yang terbesar
        return c  # Kembalikan nilai c sebagai yang terbesar

# Meminta input dari pengguna untuk tiga angka
a = float(input("Masukkan angka pertama: "))  
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

# Memanggil fungsi untuk menemukan bilangan terbesar dari a, b, dan c
largest = find_largest(a, b, c)

# Mencetak hasil bilangan terbesar
print(f"Bilangan terbesar adalah: {largest}")
