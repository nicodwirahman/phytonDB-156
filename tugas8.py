import tkinter as tk
import sqlite3
# Fungsi untuk memprediksi prodi
def hasil_prediksi():
    # Mendapatkan nilai dari input entries
    nama_siswa = nama_entry.get()
    nilai_matematika = float(input_entries[0].get())
    nilai_fisika = float(input_entries[1].get())
    nilai_kimia = float(input_entries[2].get())
    nilai_biologi = float(input_entries[3].get())
    nilai_bahasa_indonesia = float(input_entries[4].get())
    nilai_bahasa_inggris = float(input_entries[5].get())
    nilai_sejarah = float(input_entries[6].get())
    nilai_geografi = float(input_entries[7].get())
    nilai_ekonomi = float(input_entries[8].get())
    nilai_sosiologi = float(input_entries[9].get())

    # Menentukan prodi berdasarkan nilai tertinggi
    max_nilai = max(nilai_matematika, nilai_fisika, nilai_kimia, nilai_biologi, nilai_bahasa_indonesia, nilai_bahasa_inggris, nilai_sejarah, nilai_geografi, nilai_ekonomi, nilai_sosiologi)

    if max_nilai == nilai_biologi:
        hasil = "Kedokteran"
    elif max_nilai == nilai_fisika:
        hasil = "Teknik"
    elif max_nilai == nilai_bahasa_inggris:
        hasil = "Bahasa"
    else:
        hasil = "Prodi tidak dapat diprediksi"

    # Menampilkan hasil prediksi
    luaran_label.config(text=f"{nama_siswa}, prodi yang direkomendasikan: {hasil}")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("350x400")

# Membuat label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat input nilai mata pelajaran
mata_pelajaran_labels = ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Indonesia", "Bahasa Inggris", "Sejarah Indonesia", "Geografi", "Ekonomi", "Sosiologi"]
input_entries = []

for i, label_text in enumerate(mata_pelajaran_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i + 1, column=0, padx=10, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i + 1, column=1, padx=10, pady=5)
    input_entries.append(entry)

# Membuat entry untuk nama siswa
nama_label = tk.Label(root, text="Nama Siswa")
nama_label.grid(row=12, column=0, padx=10, pady=5)
nama_entry = tk.Entry(root)
nama_entry.grid(row=12, column=1, padx=10, pady=5)

# Membuat button Submit
submit_button = tk.Button(root, text="Submit", command=hasil_prediksi)
submit_button.grid(row=13, column=0, columnspan=2, pady=10)

# Membuat label luaran hasil prediksi
luaran_label = tk.Label(root, text="", font=("Arial", 14))
luaran_label.grid(row=14, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi GUI
root.mainloop()
