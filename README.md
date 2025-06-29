# ETL Assesment Task

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

6. Modul dan Penanganan Error: Membuat modul green_analysis.py untuk menghitung efisiensi CO2 dengan penanganan error ZeroDivisionError.

7. Penanganan Error dalam Loop: Menghitung rata-rata Energy_Output dengan penanganan KeyError untuk data yang hilang.

8. Bonus - Machine Learning dengan Decision Tree: Membangun model Decision Tree Classifier menggunakan scikit-learn untuk memprediksi daya tarik investasi berdasarkan fitur seperti GDP_Growth, CO2_Reduction, dan Investment_Cost.