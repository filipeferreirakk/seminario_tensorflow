"""Treino de uma rede neural para reconhecer dígitos manuscritos (MNIST)."""

import tensorflow as tf


def carregar_dados():
    """Baixa o MNIST e normaliza os pixels para a faixa 0-1."""
    (x_treino, y_treino), (x_teste, y_teste) = tf.keras.datasets.mnist.load_data()
    print(f"Treino: {x_treino.shape}  |  Teste: {x_teste.shape}")

    # Redes treinam melhor com valores pequenos: 0-255 -> 0-1
    x_treino = x_treino.astype("float32") / 255.0
    x_teste = x_teste.astype("float32") / 255.0
    return (x_treino, y_treino), (x_teste, y_teste)


if __name__ == "__main__":
    carregar_dados()