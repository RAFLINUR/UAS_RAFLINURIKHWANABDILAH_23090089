import pandas as pd
import numpy as np

data = [
    ['mahasiswa 1', 90, 80],
    ['mahasiswa 2', 50, 60],
    ['mahasiswa 3', 65, 70]
]

df = pd.DataFrame(data, columns=['Nama', 'Algoritma dan Struktur Data', 'Matematika Numerik'])
print("Dataframe:")
print(df)

rata_mata_kuliah = df[['Algoritma dan Struktur Data', 'Matematika Numerik']].mean()
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(rata_mata_kuliah)

df['Rata-rata'] = df[['Algoritma dan Struktur Data', 'Matematika Numerik']].mean(axis=1)
rata_mahasiswa = df[['Nama', 'Rata-rata']]
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(rata_mahasiswa)
