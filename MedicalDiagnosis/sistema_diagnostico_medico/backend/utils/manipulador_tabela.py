import pandas as pd

def atualizar_tabela(dados, novo_registro):
    df = pd.DataFrame(dados)
    df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
    return df.to_dict(orient="records")
