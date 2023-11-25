import tkinter as tk
import sqlite3

# Fungsi untuk memprediksi prodi dan menyimpan data ke SQLite
def hasil_prediksi():
    # Mendapatkan nilai dari input entries
    nama_siswa = input_entries[0].get()
    nilai_biologi = float(input_entries[3].get())
    nilai_fisika = float(input_entries[1].get())
    nilai_inggris = float(input_entries[5].get())

    # Menentukan prodi berdasarkan nilai tertinggi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        hasil = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        hasil = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        hasil = "Bahasa"
    else:
        hasil = "Prodi tidak dapat diprediksi"

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    # Buat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY,
            nama_siswa TEXT,
            nilai_biologi REAL,
            nilai_fisika REAL,
            nilai_inggris REAL,
            prediksi_prodi TEXT
        )
    ''')

    # Masukkan data ke dalam tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_prodi)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, hasil))

    conn.commit()
    conn.close()

    # Menampilkan hasil prediksi
    luaran_label.config(text=f"{nama_siswa}, prodi yang direkomendasikan: {hasil}")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("300x400")

# Membuat label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat input nilai mata pelajaran
mata_pelajaran_labels = ["Nama Siswa", "Matematika", "Fisika", "Biologi", "Bahasa Indonesia", "Bahasa Inggris", "Sejarah Indonesia", "Geografi", "Ekonomi", "Sosiologi"]
input_entries = []

for i, label_text in enumerate(mata_pelajaran_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i + 1, column=0, padx=10, pady=5)

    entry = tk.Entry(root)
    entry.grid(row=i + 1, column=1, padx=10, pady=5)
    input_entries.append(entry)

# Membuat button Submit
submit_button = tk.Button(root, text="Submit", command=hasil_prediksi)
submit_button.grid(row=len(mata_pelajaran_labels) + 1, column=0, columnspan=2, pady=10)

# Membuat label luaran hasil prediksi
luaran_label = tk.Label(root, text="", font=("Arial", 14))
luaran_label.grid(row=len(mata_pelajaran_labels) + 2, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi GUI
root.mainloop()
