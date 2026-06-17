"""Treino de uma rede neural para reconhecer dígitos manuscritos (MNIST)."""

import matplotlib

matplotlib.use("Agg")  # só salva imagens, sem abrir janela
import matplotlib.pyplot as plt
import tensorflow as tf


def carregar_dados():
    """Baixa o MNIST e normaliza os pixels para a faixa 0-1."""
    (x_treino, y_treino), (x_teste, y_teste) = tf.keras.datasets.mnist.load_data()
    print(f"Treino: {x_treino.shape}  |  Teste: {x_teste.shape}")

    x_treino = x_treino.astype("float32") / 255.0
    x_teste = x_teste.astype("float32") / 255.0
    return (x_treino, y_treino), (x_teste, y_teste)


def salvar_amostras(x, y, caminho="amostras.png"):
    """Salva um grid 3x3 com exemplos do dataset."""
    plt.figure(figsize=(5, 5))
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(x[i], cmap="gray")
        plt.title(f"Rótulo: {y[i]}")
        plt.axis("off")
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()
    print(f"Amostras salvas em {caminho}")


if __name__ == "__main__":
    (x_treino, y_treino), (x_teste, y_teste) = carregar_dados()
    salvar_amostras(x_treino, y_treino)