"""Treino de uma rede neural para reconhecer dígitos manuscritos (MNIST)."""

import tensorflow as tf


def carregar_dados():
    """Baixa o MNIST e separa em treino (60k) e teste (10k)."""
    (x_treino, y_treino), (x_teste, y_teste) = tf.keras.datasets.mnist.load_data()
    print(f"Treino: {x_treino.shape}  |  Teste: {x_teste.shape}")
    return (x_treino, y_treino), (x_teste, y_teste)


if __name__ == "__main__":
    carregar_dados()