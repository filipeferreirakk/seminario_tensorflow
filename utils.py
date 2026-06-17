"""
Funções de pré-processamento usadas tanto no treino quanto no app web.
Manter isso em um único lugar evita repetir lógica e garante que o
modelo receba a imagem exatamente no mesmo formato em que foi treinado.
"""

import numpy as np
from PIL import Image, ImageOps


def normalizar(x):
    """Converte os pixels de 0-255 para a faixa 0-1 (float32).

    Redes neurais treinam melhor com valores pequenos e padronizados.
    """
    return x.astype("float32") / 255.0


def preparar_imagem(imagem):
    """Recebe uma imagem PIL (o desenho do canvas) e devolve um array
    pronto para o modelo: shape (1, 28, 28), em tons de cinza e normalizado.

    Passos:
      1. Converter para tons de cinza ('L').
      2. Inverter as cores: no canvas o traço é escuro sobre fundo branco,
         mas o MNIST tem dígito branco sobre fundo preto.
      3. Redimensionar para 28x28 (tamanho que o modelo espera).
      4. Normalizar para 0-1 e adicionar a dimensão do lote (batch).
    """
    imagem = imagem.convert("L")
    imagem = ImageOps.invert(imagem)
    imagem = imagem.resize((28, 28), Image.LANCZOS)

    array = np.array(imagem)
    array = normalizar(array)
    return array.reshape(1, 28, 28)