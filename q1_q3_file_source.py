# Generate Q1 - Q3 for range generate data

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


# --- Proses untuk Economic_Dataset.xlsx ---
df_econ = pd.read_excel('Assets/Environmental_Dataset.xlsx')
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
