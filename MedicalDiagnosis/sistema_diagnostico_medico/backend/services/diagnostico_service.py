import numpy as np
from backend.models.arvore_decisao import ArvoreDecisaoID3

class DiagnosticoService:
    def __init__(self):
        self.caminho_modelo = "data/modelo_id3.pkl"
        self.modelo = ArvoreDecisaoID3.carregar_modelo(self.caminho_modelo)
        self.dados_referencia = {  # Base das doenças
            "Pipin": [2, 0, 2, 2, 0, 0, 1, 0, 0, 2, 2, 1, 2, 0, 0, 0],
            "Kafka": [0, 2, 0, 2, 2, 1, 0, 0, 2, 2, 0, 0, 0, 2, 1, 1],
            "Persico": [0, 0, 1, 0, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 0],
            "Loymo": [1, 1, 0, 1, 0, 0, 0, 2, 2, 0, 1, 2, 2, 2, 2, 2]
        }
        self.sintomas = [
            "Tosse", "Enxaqueca", "Vomito", "Diarreia", "Bulboes", "Anemia", 
            "Dores no corpo", "Inchaco nos olhos", "Paranoia", "Pneumonia",
            "Espirro", "Desmaio", "Insonia", "Tontura", "Febre", "Perda de memoria"
        ]

    def diagnosticar(self, sintomas_usuario):
        """ Diagnostica a doença com base nos sintomas informados. """
        try:
            sintomas_lista = [sintomas_usuario[s] for s in self.sintomas]
            print(f"Sintomas do usuário: {sintomas_lista}")

            melhor_doenca = None
            melhor_correspondencia = 0

            for doenca, sintomas_ref in self.dados_referencia.items():
                correspondencias = np.sum(np.array(sintomas_lista) == np.array(sintomas_ref))
                total_sintomas = len(sintomas_lista)
                percentual = (correspondencias / total_sintomas) * 100
                print(f"Doença: {doenca}, Correspondências: {correspondencias}, Percentual: {percentual}")

                if percentual > melhor_correspondencia:
                    melhor_correspondencia = percentual
                    melhor_doenca = doenca

            if melhor_correspondencia >= 86:
                return {"doenca": melhor_doenca, "status": "Internação"}
            elif melhor_correspondencia >= 70:
                return {"doenca": melhor_doenca, "status": "Observação"}
            else:
                return {"doenca": "Nenhuma", "status": "Sem diagnóstico"}
        except Exception as e:
            print(f"Erro ao diagnosticar: {e}")
            return {"doenca": None, "status": "erro"}
        