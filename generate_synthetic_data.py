import pandas as pd
import numpy as np
import random
import string

# Fungsi helper untuk generate nilai random dalam range float
def rand_float(low, high, decimals=2):
    return round(random.uniform(low, high), decimals)

# Fungsi buat Project_ID baru dengan format PLTS-REGION-XXX
def generate_project_id(existing_ids):
    # Ekstrak region unik dari data asli (bagian tengah id, contoh: PLTS-NTT-001 -> NTT)
    regions = set()
    for pid in existing_ids:
        parts = pid.split('-')
        if len(parts) >= 3:
            regions.add(parts[1])
    regions = list(regions)
    if not regions:
        regions = ['REG']  # fallback jika tidak dapat region

    new_ids = []
    count_per_region = {region:0 for region in regions}

    total_needed = 100 - len(existing_ids)

    idx = 1
    while len(existing_ids) + len(new_ids) < 100:
        for region in regions:
            count_per_region[region] += 1
            new_id = f"PLTS-{region}-{count_per_region[region]:03d}"
            if new_id not in existing_ids and new_id not in new_ids:
                new_ids.append(new_id)
            if len(existing_ids) + len(new_ids) >= 100:
                break
        idx += 1
    return new_ids

# Baca dataset
economic_df = pd.read_excel("C:\EnergiHijau2025\Assets\Economic_Dataset.xlsx")
environmental_df = pd.read_excel("C:\EnergiHijau2025\Assets\Environmental_Dataset.xlsx")
financial_df = pd.read_excel("C:\EnergiHijau2025\Assets\Financial_Dataset.xlsx")

# Ambil existing Project_ID yang ada di ketiga dataset (ambil yang common ID agar konsisten)
existing_ids = list(set(economic_df['Project_ID']).intersection(
                    environmental_df['Project_ID']).intersection(
                    financial_df['Project_ID']))

# Generate Project_ID baru agar total 100 baris
new_project_ids = generate_project_id(existing_ids)

print(f"Existing IDs: {len(existing_ids)}, New IDs to add: {len(new_project_ids)}")

# --- Definisi kategori dan range nilai sesuai rules untuk masing-masing dataset ---

# Economic dataset kategori dengan label & range
economic_categories = {
    "High: 💵💵💵💵": {"GDP_Growth": (5.35, 5.65), "Interest_Rate": (1.9, 3.9), "Bond_Yield": (4.85,4.95)},
    "High: 💵💵💵💵💵": {"GDP_Growth": (6.05, 6.15), "Interest_Rate": (0.95, 2.85), "Bond_Yield": (4.85,4.95)},
    "Low: 💵💵": {"GDP_Growth": (4.0, 4.5), "Interest_Rate": (4.5, 4.7), "Bond_Yield": (5.3,5.45)},
    "Medium: 💵💵💵": {"GDP_Growth": (4.65, 4.85), "Interest_Rate": (4.0, 4.23), "Bond_Yield": (5.0,5.12)},
}

# Environmental dataset kategori dengan label & range
environmental_categories = {
    "High: 🌿🌿🌿🌿": {"CO2_Reduction": (67500, 77500), "Energy_Output": (22500, 26500), "Environmental_Risk_Index": (37.5, 42.5)},
    "High: 🌿🌿🌿🌿🌿": {"CO2_Reduction": (91250, 93750), "Energy_Output": (30500, 31500), "Environmental_Risk_Index": (26.25, 28.75)},
    "Medium: 🌿🌿🌿": {"CO2_Reduction": (32000, 36000), "Energy_Output": (11000, 13000), "Environmental_Risk_Index": (55, 65)},
}

# Financial dataset kategori dengan label & range
financial_categories = {
    "High: ★★★★★": {"Investment_Cost": (100, 105), "Revenue_Stream": (8, 9.5), "Debt_Ratio": (0.75, 0.85), "Payment_Delay": (60, 62.5)},
    "High: ★★★★☆": {"Investment_Cost": (205.1725, 215.0575), "Revenue_Stream": (18.5, 19.5), "Debt_Ratio": (0.705,0.715), "Payment_Delay": (41.25,43.75)},
    "Low: ★★☆☆☆": {"Investment_Cost": (81.25, 83.75), "Revenue_Stream": (6.575, 6.725), "Debt_Ratio": (0.5575, 0.5725), "Payment_Delay": (12.75,14.25)},
    "Low: ★☆☆☆☆": {"Investment_Cost": (125.5, 130.5), "Revenue_Stream": (10, 11), "Debt_Ratio": (0.5, 0.7), "Payment_Delay": (10,11)},
    "Medium: ★★★☆☆": {"Investment_Cost": (93.75, 157.5), "Revenue_Stream": (7.425, 13.125), "Debt_Ratio": (0.615, 0.6575), "Payment_Delay": (19.5, 26.25)},
}

# Fungsi buat baris baru economic
def create_economic_row(project_id):
    cat = random.choice(list(economic_categories.keys()))
    vals = economic_categories[cat]
    return {
        "Project_ID": project_id,
        "Daya_Tarik_Investasi": cat,
        "GDP_Growth": rand_float(*vals["GDP_Growth"]),
        "Interest_Rate": rand_float(*vals["Interest_Rate"]),
        "Bond_Yield": rand_float(*vals["Bond_Yield"]),
    }

# Fungsi buat baris baru environmental
def create_environmental_row(project_id):
    cat = random.choice(list(environmental_categories.keys()))
    vals = environmental_categories[cat]
    return {
        "Project_ID": project_id,
        "Peringkat_Dampak": cat,
        "CO2_Reduction": rand_float(*vals["CO2_Reduction"]),
        "Energy_Output": rand_float(*vals["Energy_Output"]),
        "Environmental_Risk_Index": rand_float(*vals["Environmental_Risk_Index"]),
    }

# Fungsi buat baris baru financial
def create_financial_row(project_id):
    cat = random.choice(list(financial_categories.keys()))
    vals = financial_categories[cat]
    return {
        "Project_ID": project_id,
        "Status_Rank": cat,
        "Investment_Cost": rand_float(*vals["Investment_Cost"]),
        "Revenue_Stream": rand_float(*vals["Revenue_Stream"]),
        "Debt_Ratio": rand_float(*vals["Debt_Ratio"], decimals=3),
        "Payment_Delay": rand_float(*vals["Payment_Delay"]),
    }

# Buat list baris baru untuk ketiga dataset berdasarkan new_project_ids
economic_new_rows = [create_economic_row(pid) for pid in new_project_ids]
environmental_new_rows = [create_environmental_row(pid) for pid in new_project_ids]
financial_new_rows = [create_financial_row(pid) for pid in new_project_ids]

# Gabungkan dataframe lama dengan data baru
economic_df_extended = pd.concat([economic_df, pd.DataFrame(economic_new_rows)], ignore_index=True)
environmental_df_extended = pd.concat([environmental_df, pd.DataFrame(environmental_new_rows)], ignore_index=True)
financial_df_extended = pd.concat([financial_df, pd.DataFrame(financial_new_rows)], ignore_index=True)

# Simpan hasil ke file Excel baru
economic_df_extended.to_excel('output_Economic_Dataset_Extended.xlsx', index=False)
environmental_df_extended.to_excel('output_Environmental_Dataset_Extended.xlsx', index=False)
financial_df_extended.to_excel('output_Financial_Dataset_Extended.xlsx', index=False)

print("Dataset berhasil diperluas hingga 100 baris per file dan disimpan dengan nama 'out_*.xlsx'.")

