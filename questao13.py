import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = {
    "usuario": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "idade": [18, 22, 25, 31, 28, 35, 42, 24, 29, 33],
    "requisicoes": [10, 15, 8, 20, 12, 25, 18, 9, 14, 21],
    "tempo_ms": [120, 130, 115, 140, 125, 150, 135, 110, 128, 145],
    "erros": [0, 1, 0, 2, 0, 3, 1, 0, 1, 2],
    "sistema": ["Android", "iOS", "Android", "Android", "iOS",
                "Android", "Windows", "Android", "iOS", "Android"],
}
df = pd.DataFrame(dados)

total = len(df)
n_android = (df["sistema"] == "Android").sum()
n_ios = (df["sistema"] == "iOS").sum()
n_nao_android = (df["sistema"] != "Android").sum()

print(f"a) P(Android)     = {n_android}/{total} = {n_android / total:.2f}")
print(f"b) P(iOS)         = {n_ios}/{total} = {n_ios / total:.2f}")
print(f"c) P(não Android) = {n_nao_android}/{total} = {n_nao_android / total:.2f}")