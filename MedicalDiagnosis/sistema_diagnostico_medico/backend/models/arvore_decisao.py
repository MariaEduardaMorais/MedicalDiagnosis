import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

MAPEAMENTO_SINTOMAS = {"Irrelevante": 0, "Médio": 1, "Forte": 2}

class ArvoreDecisaoID3:
    def __init__(self):
        self.modelo = DecisionTreeClassifier(criterion="entropy")

    def treinar(self, dados):
        df = pd.DataFrame(dados)
        df.replace(MAPEAMENTO_SINTOMAS, inplace=True)
        X = df.drop(columns=["Doença"])
        y = df["Doença"]
        self.modelo.fit(X, y)
        print("Modelo treinado com sucesso.")
        print(f"Features: {X.columns.tolist()}")
        print(f"Classes: {self.modelo.classes_}")

    def salvar_modelo(self, caminho):
        with open(caminho, "wb") as f:
            pickle.dump(self.modelo, f)
        print(f"Modelo salvo em {caminho}.")

    @staticmethod
    def carregar_modelo(caminho):
        with open(caminho, "rb") as f:
            modelo = pickle.load(f)
        print(f"Modelo carregado de {caminho}.")
        return modelo

    def calcular_diagnostico(self, sintomas):
        sintomas_numericos = [MAPEAMENTO_SINTOMAS[sintoma] for sintoma in sintomas]
        diagnostico = self.modelo.predict([sintomas_numericos])
        print(f"Sintomas: {sintomas} -> Diagnóstico: {diagnostico[0]}")
        return diagnostico[0]
    