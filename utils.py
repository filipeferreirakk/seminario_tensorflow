"""Funções de pré-processamento compartilhadas (treino e app)."""

import numpy as np


def normalizar(x):
    """Converte os pixels de 0-255 para a faixa 0-1 (float32).
    Redes neurais treinam melhor com valores pequenos e padronizados.
    """
    return x.astype("float32") / 255.0