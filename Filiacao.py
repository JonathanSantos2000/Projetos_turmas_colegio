import pandas as pd
import os

lista_arquivo = os.listdir('Turmas')
nmTabela = lista_arquivo


for i, arquivo in enumerate(lista_arquivo):
    nmTabela[i] = pd.read_excel(f"Turmas/{arquivo}")

familia = pd.concat(nmTabela, ignore_index=True)
familia['Nome'] = familia['Nome'] + ", "
familia = familia.dropna(how="any", axis=0)
familia = familia.rename(columns={'Mae/Pai': 'Mãe'})
familia = familia.rename(columns={'Nome': 'Alunos'})

tabela_familia = familia.groupby('Mãe').sum()
tabela_familia = tabela_familia[['Alunos']]

tabela_familia.to_excel('Tabela-familias.xlsx')

