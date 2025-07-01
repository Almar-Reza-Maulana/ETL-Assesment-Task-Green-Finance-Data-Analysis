# ETL Assesment Task
## 👥 Kelompok & Anggota
Repositori ini dibuat oleh Kelompok 4 sebagai bagian dari mengerjakan tugas yang diberikan , dengan tujuan ........

| Nama            | No Absen       | Kelompok |
|------------------|----------------|----------|
| Doni Wahyudi     | 9.043.DB2025   | 4        |      
| Farhan Fadillah  | 9.008.DB2025   | 4        |
| Almar Reza Maulana  | 9.043.DB2025  | 4      |


---
## Latar Belakang
Tugas ini berfokus pada analisis data dari berbagai dataset yang mencakup aspek ekonomi, sosial, lingkungan, geospasial, dan keuangan terkait proyek energi terbarukan, khususnya PLTS (Pembangkit Listrik Tenaga Surya) dan PLTM (Pembangkit Listrik Tenaga Mikrohidro). Dataset yang digunakan meliputi:

1. Economic Dataset: Berisi informasi seperti GDP_Growth dan Daya_Tarik_Investasi (High, Medium, Low) untuk menilai daya tarik ekonomi proyek.

2. Social Dataset: Mencakup Land_Status (Adat, Negara, Swasta) dan Tingkat_Konflik (High, Medium, Low) untuk mengevaluasi risiko sosial.

3. Environmental Dataset: Berfokus pada CO2_Reduction (ton CO2e) dan Energy_Output (MWh) untuk mengukur dampak lingkungan.

4. Geospatial Dataset: Menyediakan data Efisiensi_Lokasi (High, Medium, Low) berdasarkan faktor seperti iradiasi matahari atau kedekatan dengan jaringan listrik.

5. Financial Dataset: Berisi Investment_Cost (dalam miliar rupiah) untuk menilai skala keuangan proyek.

---
## Tujuan dan Lingkup 
Tugas ini terdiri dari tujuh soal utama dan satu soal bonus, yang masing-masing menguji kemampuan kami dalam berbagai aspek pemrograman Python dan analisis data:

1. Conditional Statements (IF-Else) dan Operasi Aritmatika: Menghitung efisiensi pengurangan CO2 per juta rupiah untuk proyek PLTS.

2. For Loop dan Lists: Menghitung rata-rata pengurangan CO2 untuk proyek PLTM.

3. Input Pengguna dan Kontrol Loop: Menangani input Project_ID untuk analisis data sosial dengan loop yang berhenti saat input "DONE".

4. Dictionary dan Pemfilteran Kondisional: Mengidentifikasi proyek dengan daya tarik investasi tinggi dan risiko konflik sosial rendah.

5. Kemampuan analisis data tambahan.
   
---
## Pendekatan dan Metodologi 

Kami bekerja secara kolaboratif untuk menyelesaikan tugas ini, memanfaatkan keahlian masing-masing anggota tim dalam pemrograman Python, pengelolaan data dengan pandas, dan analisis machine learning dengan scikit-learn. Pendekatan kami meliputi :

1. Pembersihan dan Integrasi Data : Menggabungkan dataset berdasrkan Project_ID untuk analisis lintas domain.

2. Pemrograman Terstruktur : Menggunakan struktur kode yang rapi disertai komentar yang jelas untuk memudahkan pemahaman.

3. Penanganan Error : Menerapkan try-except untuk menangani potensi error seperti pembagian dengan nol atau data yang hilang.

4. Analisis Machine Learning : Membangun model prediktif dengan Decision Tree Classifier untuk mendukung pengambilan keputusan investasi.

7. Modul dan Penanganan Error: Membuat modul green_analysis.py untuk menghitung efisiensi CO2 dengan penanganan error ZeroDivisionError.

8. Penanganan Error dalam Loop: Menghitung rata-rata Energy_Output dengan penanganan KeyError untuk data yang hilang.

9. Bonus - Machine Learning dengan Decision Tree: Membangun model Decision Tree Classifier menggunakan scikit-learn untuk memprediksi daya tarik investasi berdasarkan fitur seperti GDP_Growth, CO2_Reduction, dan Investment_Cost.
