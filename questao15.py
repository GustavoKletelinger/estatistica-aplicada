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

# a) Estatística descritiva
media = df["tempo_ms"].mean()
mediana = df["tempo_ms"].median()
amplitude = df["tempo_ms"].max() - df["tempo_ms"].min()
desvio = df["tempo_ms"].std(ddof=0)   # populacional, como nas questões 8 e 9

print("a) ESTATÍSTICA DESCRITIVA (tempo_ms)")
print(f"   Média:         {media:.2f} ms")
print(f"   Mediana:       {mediana:.2f} ms")
print(f"   Amplitude:     {amplitude} ms")
print(f"   Desvio padrão: {desvio:.2f} ms")

# b) Frequência
freq = df["sistema"].value_counts()
perc = df["sistema"].value_counts(normalize=True) * 100
print("\nb) DISTRIBUIÇÃO POR SISTEMA OPERACIONAL")
for sistema in freq.index:
    print(f"   {sistema:<8} {freq[sistema]} usuários ({perc[sistema]:.0f}%)")

# c) Probabilidade
p_erro = (df["erros"] > 0).mean()
print("\nc) PROBABILIDADE ESTIMADA DE ERRO")
print(f"   P(erro) = {(df['erros'] > 0).sum()}/{len(df)} = {p_erro:.2f} ({p_erro * 100:.0f}%)")

# d) Visualização
fig, eixos = plt.subplots(1, 2, figsize=(12, 5))

barras = eixos[0].bar(freq.index, freq.values,
                      color=["#3ddc84", "#555555", "#0078d4"])
eixos[0].set_title("Distribuição dos sistemas operacionais")
eixos[0].set_xlabel("Sistema operacional")
eixos[0].set_ylabel("Quantidade de usuários")
eixos[0].bar_label(barras)

eixos[1].hist(df["tempo_ms"], bins=5, color="#e50914", edgecolor="white")
eixos[1].axvline(media, color="black", linestyle="--", label=f"Média = {media:.1f} ms")
eixos[1].set_title("Distribuição dos tempos de resposta")
eixos[1].set_xlabel("Tempo de resposta (ms)")
eixos[1].set_ylabel("Frequência")
eixos[1].legend()

plt.tight_layout()
plt.savefig("graficos_questao15.png", dpi=150)
plt.show()