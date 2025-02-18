import sys
import os
from flask_cors import CORS
import traceback
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from backend.models.arvore_decisao import ArvoreDecisaoID3
from backend.services.diagnostico_service import DiagnosticoService

app = Flask(__name__)
app = Flask(__name__)
CORS(app)

dados_iniciais = {
    "Doença": ["Pipin", "Kafka", "Persico", "Loymo"],
    "Tosse": [2, 0, 0, 1],
    "Enxaqueca": [0, 2, 0, 1],
    "Vomito": [2, 0, 1, 0],
    "Diarreia": [2, 2, 0, 1],
    "Bulboes": [0, 2, 2, 0],
    "Anemia": [0, 1, 2, 0],
    "Dores no corpo": [1, 0, 2, 0],
    "Inchaco nos olhos": [0, 0, 2, 2],
    "Paranoia": [0, 2, 1, 2],
    "Pneumonia": [2, 2, 0, 0],
    "Espirro": [2, 0, 0, 1],
    "Desmaio": [1, 0, 0, 2],
    "Insonia": [2, 0, 0, 2],
    "Tontura": [0, 2, 1, 2],
    "Febre": [0, 1, 2, 2],
    "Perda de memoria": [0, 1, 0, 2]
}

arvore = ArvoreDecisaoID3()
arvore.treinar(dados_iniciais)

if not os.path.exists('data'):
    os.makedirs('data')

arvore.salvar_modelo("data/modelo_id3.pkl")

servico_diagnostico = DiagnosticoService()

@app.route("/diagnostico", methods=["POST"])
def diagnostico():
    try:
        dados = request.get_json()
        print(f"Dados recebidos: {dados}")
        sintomas = dados.get("sintomas", {})
        print(f"Recebido sintomas: {sintomas}")

        resultado = servico_diagnostico.diagnosticar(sintomas)
        print(f"Resultado do diagnóstico: {resultado}")

        return jsonify({"diagnostico": resultado["doenca"], "status": resultado["status"]})

    except Exception as e:
        print(f"Erro no servidor: {e}")
        traceback.print_exc()
        return jsonify({"erro": "Erro ao processar diagnóstico"}), 500

if __name__ == '__main__':
    app.run(debug=True)