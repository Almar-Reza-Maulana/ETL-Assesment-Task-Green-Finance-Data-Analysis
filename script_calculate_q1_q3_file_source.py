# Cara Kerja Proses Script
# Definisi fungsi:
# Fungsi calculate_q1_q3_grouped menerima tiga parameter: data frame (df), nama kolom grup (group_col), dan daftar kolom numerik (numeric_cols) yang ingin dihitung kuartilnya. Fungsi ini melakukan:

# Pengelompokan data berdasarkan group_col.
# Menghitung kuartil pertama (Q1, 25%) dan kuartil ketiga (Q3, 75%) untuk kolom numerik tersebut.
# Menyesuaikan format hasil agar konsisten menjadi DataFrame dengan kolom yang diberi nama dengan prefix Q1_ dan Q3_ untuk membedakan.
# Menggabungkan hasil Q1 dan Q3 menjadi satu DataFrame hasil akhir.

# Loading dataset:
# Script membaca tiga file Excel yang berbeda:
# Economic_Dataset.xlsx
# Environmental_Dataset.xlsx
# Financial_Dataset.xlsx 

# Setiap dataset memiliki kolom numerik dan kolom kategori tertentu yang dipakai sebagai basis grup.
# Pemrosesan masing-masing dataset:

# Di setiap dataset, script menentukan kolom numerik yang valid di dataset tersebut.
# Menggunakan fungsi calculate_q1_q3_grouped untuk menghitung Q1 dan Q3 berdasar kolom grup yang relevan.
# Menyimpan hasilnya ke file Excel output yang berbeda seperti out_q1_q3_economic.xlsx dan seterusnya.

# Output:
# File Excel yang berisi nilai Q1 dan Q3 untuk setiap grup kategori pada kolom numerik yang dipilih, memudahkan analisis data kuantitatif berdasarkan kategori yang diinginkan.

# Tujuan Script
# Menganalisis distribusi statistika kuartil dari data numerik dalam kelompok tertentu, sehingga tiap grup kategori (seperti tingkat daya tarik investasi, peringkat dampak lingkungan, atau status finansial) dapat dilihat tren distribusinya.
# Membantu pengambilan keputusan berbasis segmentasi data dengan memberikan pemahaman lengkap pada variasi statistik numerik berdasarkan grup.
# Mempersiapkan data ringkasan dalam format Excel yang mudah diakses dan digunakan untuk laporan atau analisis lanjutan.



import pandas as pd

def calculate_q1_q3_grouped(df, group_col, numeric_cols):
    # Group dan hitung Q1
    q1 = df.groupby(group_col)[numeric_cols].quantile(0.25)
    # Jika hasil Q1 adalah Series (karena 1 kolom numeric), convert menjadi DataFrame
    if isinstance(q1, pd.Series):
        q1 = q1.to_frame()
    q1.columns = [f"Q1_{col}" for col in q1.columns]

    # Group dan hitung Q3
    q3 = df.groupby(group_col)[numeric_cols].quantile(0.75)
    if isinstance(q3, pd.Series):
        q3 = q3.to_frame()
    q3.columns = [f"Q3_{col}" for col in q3.columns]

    # Gabungkan hasil Q1 dan Q3 menjadi satu DataFrame
    result = pd.concat([q1, q3], axis=1).reset_index()
    return result

# Argument:
# - df adalah DataFrame pandas yang berisi data.
# - group_col adalah nama kolom yang dipakai untuk mengelompokkan data.
# - numeric_cols adalah list kolom yang berisi data numerik untuk dihitung kuartilnya.

# Proses utama:
# - df.groupby(group_col)[numeric_cols]: Mengelompokkan data berdasarkan kolom grup (misalnya kategori).
# - .quantile(0.25) dan .quantile(0.75): Menghitung kuartil pertama (Q1) dan kuartil ketiga (Q3).
# - Cek apakah hasil berupa Series (biasanya kalau hanya satu kolom), jika iya, diubah ke DataFrame agar konsisten.
# - Ganti nama kolom hasil dengan prefix "Q1_" atau "Q3_" agar bisa membedakan antara kuartil pertama dan ketiga.
# - Gabungkan kedua DataFrame hasil kuartil jadi satu per grup kategori dengan pd.concat dan reset index supaya hasil rapi.'

# --- Proses untuk Economic_Dataset.xlsx ---
df_econ = pd.read_excel('Assets\Economic_Dataset.xlsx')
econ_numeric_cols = ['GDP_Growth', 'Interest_Rate', 'Bond_Yield']
econ_numeric_cols = [col for col in econ_numeric_cols if col in df_econ.columns]
econ_group_col = 'Daya_Tarik_Investasi'

econ_q1_q3 = calculate_q1_q3_grouped(df_econ, econ_group_col, econ_numeric_cols)
econ_q1_q3.to_excel('out_q1_q3_economic.xlsx', index=False)
print("Finished Q1 & Q3 calculation for Economic_Dataset")

# --- Proses untuk Environmental_Dataset.xlsx ---
df_env = pd.read_excel('Assets\Environmental_Dataset.xlsx')
env_numeric_cols = ['CO2_Reduction', 'Energy_Output', 'Environmental_Risk_Index']
env_numeric_cols = [col for col in env_numeric_cols if col in df_env.columns]
env_group_col = 'Peringkat_Dampak'

env_q1_q3 = calculate_q1_q3_grouped(df_env, env_group_col, env_numeric_cols)
env_q1_q3.to_excel('out_q1_q3_environmental.xlsx', index=False)
print("Finished Q1 & Q3 calculation for Environmental_Dataset")

# --- Proses untuk Financial_Dataset.xlsx ---
df_fin = pd.read_excel('Assets\Financial_Dataset.xlsx')
fin_numeric_cols = ['Investment_Cost', 'Revenue_Stream', 'Debt_Ratio', 'Payment_Delay']
fin_numeric_cols = [col for col in fin_numeric_cols if col in df_fin.columns]
fin_group_col = 'Status_Rank'

fin_q1_q3 = calculate_q1_q3_grouped(df_fin, fin_group_col, fin_numeric_cols)
fin_q1_q3.to_excel('out_q1_q3_financial.xlsx', index=False)
print("Finished Q1 & Q3 calculation for Financial_Dataset")

print("All tasks completed. Output files have been saved.")
