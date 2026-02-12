import pandas as pd

# 1. Load dataset 
file_path = 'Data/Rawdata.csv' 
df = pd.read_csv(file_path)

# Cek jumlah data asli
print(f"Jumlah data asli: {len(df)} baris")

# 2. Lakukan Random Sampling
df_sample = df.sample(n=1000, random_state=42)

# Cek jumlah data setelah dipotong
print(f"Jumlah data setelah dipotong: {len(df_sample)} baris")

# 3. Simpan hasil ke file baru (agar file asli tidak tertimpa)
df_sample.to_csv('indonesia_news_sample_1000.csv', index=False)

print("Berhasil! File baru 'indonesia_news_sample_1000.csv' telah dibuat.")