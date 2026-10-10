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

quantidade = df["sistema"].value_counts()

plt.figure(figsize=(7, 5))
barras = plt.bar(quantidade.index, quantidade.values,
                 color=["#3ddc84", "#555555", "#0078d4"])
plt.title("Quantidade de usuários por sistema operacional")
plt.xlabel("Sistema operacional")
plt.ylabel("Quantidade de usuários")
plt.bar_label(barras)
plt.tight_layout()
plt.savefig("grafico_sistemas_q6.png", dpi=150)
plt.show()

print("Maior frequência:", quantidade.idxmax(), "-", quantidade.max(), "usuários")