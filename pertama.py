def evaluate_performance(percentage):  # Membuat fungsi untuk mengevaluasi kinerja berdasarkan persentase nilai
    if percentage >= 90:  # Jika persentase >= 90, kinerja dianggap "Excellent"
        return "Excellent performance"
    elif percentage >= 80:  # Jika persentase antara 80 dan 89, kinerja dianggap "Very Good"
        return "Very Good performance"
    elif percentage >= 70:  # Jika persentase antara 70 dan 79, kinerja dianggap "Good"
        return "Good performance"
    elif percentage >= 60:  # Jika persentase antara 60 dan 69, kinerja dianggap "Average"
        return "Average performance"
    else:  # Jika persentase < 60, kinerja dianggap "Below Average"
        return "Below average performance"

# Meminta input dari pengguna untuk persentase nilai siswa
percentage = float(input("Masukkan persentase nilai siswa: "))

# Memanggil fungsi untuk mengevaluasi kinerja siswa berdasarkan persentase
result = evaluate_performance(percentage)

# Mencetak hasil evaluasi kinerja siswa
print(result)
