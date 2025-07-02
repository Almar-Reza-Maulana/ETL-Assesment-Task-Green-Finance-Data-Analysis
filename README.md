# ETL Assesment Task

Repositori ini dibuat oleh Kelompok 4 untuk memenuhi soal ujian yang diberikan untuk menguasai pemrograman Python dan analisis data dalam konteks Green Finance serta proyek energi terbarukan di Indonesia tahun 2025. Dengan semangat inovasi dan kolaborasi, kami berupaya menghasilkan karya yang tidak hanya memenuhi standar, tetapi juga mencerminkan dedikasi kami untuk mendukung pembangunan berkelanjutan Indonesia melalui inisiatif Green Finance.

---
### 👥 Kelompok & Anggota

| Nama            | No Absen       | Kelompok |
|------------------|----------------|----------|
| Doni Wahyudi     | 9.043.DB2025   | 4        |      
| Farhan Fadillah  | 9.008.DB2025   | 4        |
| Almar Reza Maulana  | 9.043.DB2025  | 4      |

---
## BAB 1 PENDAHULUAN

### 1.1 Latar Belakang
Sektor energi terbarukan di indonesia terus berkembang pesat sebagai bagian dari komitmen negara terhadap pembangunan berkelanjutan dan inisiatif keuangan hijau. Dalam konteks ini, analisis data yang akurat dan efisien menjadi krusial untuk mengevaluasi proyek-proyek, mengidentifikasi peluang investasi, serta memitigasi risiko sosial dan lingkungan. Tugas ini berfokus pada analisis data dari berbagai dataset yang mencakup aspek ekonomi, sosial, lingkungan, geospasial, dan keuangan terkait proyek energi terbarukan, khususnya PLTS (Pembangkit Listrik Tenaga Surya) dan PLTM (Pembangkit Listrik Tenaga Mikrohidro). Dataset yang digunakan meliputi:

1. Economic Dataset: Berisi informasi seperti GDP_Growth dan Daya_Tarik_Investasi (High, Medium, Low) untuk menilai daya tarik ekonomi proyek.

2. Social Dataset: Mencakup Land_Status (Adat, Negara, Swasta) dan Tingkat_Konflik (High, Medium, Low) untuk mengevaluasi risiko sosial.

3. Environmental Dataset: Berfokus pada CO2_Reduction (ton CO2e) dan Energy_Output (MWh) untuk mengukur dampak lingkungan.

4. Geospatial Dataset: Menyediakan data Efisiensi_Lokasi (High, Medium, Low) berdasarkan faktor seperti radiasi matahari atau kedekatan dengan jaringan listrik.

5. Financial Dataset: Berisi Investment_Cost (dalam miliar rupiah) untuk menilai skala keuangan proyek.

---
### 1.2 Identifikasi Masalah 
Berdasarkan dari tugas ini dan kebutuhan analisis data dalam konteks green finance di indonesia, ada beberapa masalah utama yang di dapat yaitu :

1. Efisiensi Pengurangan CO2 Proyek PLTS : Pemerintah perlu mengidentifikasi proyek PLTS yang mempunyai efisiensi pengurangan emisi CO2 tinggi per unit investasi, dihitung sebagai rasio pengurangan CO2 perjuta rupiah.

2. Dampak Lingkungan Kolektif Proyek PLTM : Pemerintah memebutuhkan informasi mengenai rata-rata penguranagan CO2 dari proyek PLTM untuk menilai dampak lingkungan keseluruhannya.

3. Akses informasi Status Lahan dan Konflik Sosial : Diperlukan alat yang efisien untuk memverifikasi status lahan dan konflik sosial suatu proyek berdasarkan ``Project_ID`` yang diinput oleh pengguna. Sistem juga harus bisa menangani apakah ``Project_ID`` valid atau tidak valid.

4. Identifikasi Proyek Minim Risiko : Pemerintah mencari proyek dengan daya tarik investasi tinggi dan tingkat konflik sosial yang rendah untuk meminimalisir adanya resiko.

5. Total Investasi Berdasarkan efisiensi lokasi : Diperlukan perhitungan total investasi untuk proyek-proyek yang memiliki efisiensi tinggi.

6. Penanganan Kesalahan dalam perhitungan Efisiensi CO2 : Diperlukan modul yang dapat digunakan kembali untuk menghitung efisiensi pengurangan CO2 per investasi (masih belum paham nanti ditanya)

7. Pengerjaan niali rata-rata dengan data yang tidak ada : Diperlukan perhitungan rata-rata output energi dari proyek yang terpilih, namun harus bisa mengelola data yang hilang di ``Project_ID``

   
---
### 1.3 Rumusan Masalah
Berdasarkan identifikasi masalah di atas, perumusan masalah dari tugas asesmen ini adalah sebagai berikut:

Bagaimana cara mengembangkan solusi berbasis Python untuk melakukan analisis data Keuangan Hijau di Indonesia, yang mencakup:

1. Penggabungan dan filtering dataset untuk mengidentifikasi proyek PLTS dengan efisiensi pengurangan CO2 yang tinggi per unit investasi, serta mengklasifikasikannya sebagai "High" atau "Low"?

2.  Menghitung rata-rata pengurangan CO2 untuk proyek PLTM menggunakan perulangan (for loop) dan list?

3. Membuat program interaktif menggunakan perulangan (while loop) untuk memeriksa status lahan dan tingkat konflik sosial proyek berdasarkan input Project_ID dari pengguna, termasuk penanganan ``Project_ID`` yang tidak valid?

4. Memfilter dan menampilkan ``Project_ID`` dari proyek-proyek yang memiliki daya tarik investasi "High" dan tingkat konflik "Low" melalui penggabungan dataset dan operasi dictionary?

5. Mendefinisikan dan menggunakan fungsi untuk menghitung total investasi proyek yang memiliki efisiensi lokasi "High" dari dataset gabungan?

6. Mengembangkan modul Python terpisah dengan fungsi yang menghitung efisiensi pengurangan CO2 per investasi, lengkap dengan penanganan ZeroDivisionError?

7. Menerapkan penanganan kesalahan (try-except) dalam perulangan (for loop) untuk menghitung rata-rata output energi proyek, meskipun terdapat ``Project_ID`` yang hilang?

8. Membangun dan mengevaluasi model Decision Tree Classifier menggunakan scikit-learn untuk memprediksi daya tarik investasi proyek baru berdasarkan fitur ekonomi, lingkungan, dan keuangan?

---
## BAB II PEMBAHASAN
Bab ini akan membahas implementasi solusi untuk setiap pertanyaandi soal, mulai dari konsep dasar Python hingga aplikasi Machine Learning. Setiap sub-bab akan menjelaskan pendekatan, kode, dan contoh output yang diharapkan.

---
### 2.1 Question 1 : Conditional Statements (If-Else) and Arithmetic Operations
(isi jawaban dan pembahasannya)

---
### 2.2 Question 2: For Loop and Lists
(isi jawaban dan pembahasannya)

---
### 2.3 Question 3: While Loop and User Input
(isi jawaban dan pembahasannya)

---
### 2.4 Question 4: Dictionary and Conditional Filtering
(isi jawaban dan pembahasannya)

---
### 2.5 Question 5: Functions and Arithmetic
(isi jawaban dan pembahasannya)

---
### 2.6 Question 6: Modules and Error Handling
(isi jawaban dan pembahasannya)

---
### 2.7 Question 7: Error Handling in Loops
(isi jawaban dan pembahasannya)

---
### 2.8 Bonus Question: Machine Learning/AI with Decision Tree
(isi jawaban dan pembahasannya)

---
## BAB III PENUTUP
Sebagai bagian akhir dari repositori ini, maka dalam bab 3 ini akan disampaikan kesimpulan, dan saran mengenai hasil pengerjaan yang telah kami kerjakan. Kesimpulan, dan saran tersebut adalah sebagai berikut:
---
### 3.1 Kesimpulan

---
### 3.2 Saran 
