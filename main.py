import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tabela = pd.read_csv("base_clientes.csv")

linhas_iniciais = len(tabela)
tabela = tabela.drop_duplicates()

tabela = tabela.dropna()

linhas_finais = len(tabela)
print("Linhas iniciais:", linhas_iniciais, " - Linhas Finais:", linhas_finais)

resumo = tabela.describe(include="all")
correlacoes = tabela.corr(numeric_only=True)
                          
with pd.ExcelWriter("Resumo.xlsx") as arquivo:
    resumo.to_excel(arquivo, sheet_name="resumo")
    correlacoes.to_excel(arquivo, sheet_name="correlacao")

tabela.hist(figsize=(12, 8),bins=20, color="skyblue", edgecolor="black")
plt.suptitle("Distribuição das Variáveis Numéricas", fontsize=16)
plt.tight_layout()
plt.savefig("histogramas.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(correlaçoes, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Mapa de Calor - Correlação das Variáveis", fontsize=16)
plt.tight_layout()
plt.savefig("heatmap.png")  # 🔵 salva como imagem
plt.show()