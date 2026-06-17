"""
App web do demo: serve a página com o canvas e expõe o endpoint /prever,
que recebe o desenho, passa pelo modelo treinado e devolve o dígito previsto
junto com a confiança de cada classe.

Execute com:  python app.py
Depois abra:  http://127.0.0.1:5000
"""

import base64
import io

import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from PIL import Image

from utils import preparar_imagem

app = Flask(__name__)

# Carrega o modelo uma única vez, quando o servidor sobe.
modelo = tf.keras.models.load_model("mnist_model.keras")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/prever", methods=["POST"])
def prever():
    # O canvas envia a imagem como Data URL (base64). Removemos o cabeçalho
    # "data:image/png;base64," e decodificamos os bytes da imagem.
    dados = request.get_json()
    cabecalho, codificado = dados["imagem"].split(",", 1)
    bytes_imagem = base64.b64decode(codificado)
    imagem = Image.open(io.BytesIO(bytes_imagem))

    entrada = preparar_imagem(imagem)
    probabilidades = modelo.predict(entrada, verbose=0)[0]

    digito = int(np.argmax(probabilidades))
    confianca = float(np.max(probabilidades))

    return jsonify(
        {
            "digito": digito,
            "confianca": confianca,
            "probabilidades": [float(p) for p in probabilidades],
        }
    )


if __name__ == "__main__":
    app.run(debug=True)