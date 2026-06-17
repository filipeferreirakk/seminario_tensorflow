"""Treino de uma rede neural para reconhecer dígitos manuscritos (MNIST)."""

import matplotlib

matplotlib.use("Agg")  # só salva imagens, sem abrir janela
import matplotlib.pyplot as plt
import tensorflow as tf

from utils import normalizar

EPOCAS = 5
CAMINHO_MODELO = "mnist_model.keras"


def carregar_dados():
    """Baixa o MNIST e normaliza os pixels para a faixa 0-1."""
    (x_treino, y_treino), (x_teste, y_teste) = tf.keras.datasets.mnist.load_data()
    print(f"Treino: {x_treino.shape}  |  Teste: {x_teste.shape}")

    x_treino = normalizar(x_treino)
    x_teste = normalizar(x_teste)
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


def construir_modelo():
    """Define a arquitetura da rede:
      Flatten -> Dense(128, relu) -> Dropout(0.2) -> Dense(10, softmax).
    O Dropout desliga 20% dos neurônios no treino para evitar overfitting.
    """
    modelo = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(28, 28)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    modelo.summary()
    return modelo


def plotar_historico(historico, caminho="historico.png"):
    """Gera as curvas de acurácia e perda ao longo das épocas."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(historico.history["accuracy"], label="treino")
    ax1.plot(historico.history["val_accuracy"], label="validação")
    ax1.set_title("Acurácia")
    ax1.set_xlabel("Época")
    ax1.legend()

    ax2.plot(historico.history["loss"], label="treino")
    ax2.plot(historico.history["val_loss"], label="validação")
    ax2.set_title("Perda")
    ax2.set_xlabel("Época")
    ax2.legend()

    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()
    print(f"Histórico salvo em {caminho}")


if __name__ == "__main__":
    (x_treino, y_treino), (x_teste, y_teste) = carregar_dados()
    salvar_amostras(x_treino, y_treino)

    modelo = construir_modelo()
    modelo.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    historico = modelo.fit(x_treino, y_treino, epochs=EPOCAS, validation_split=0.1)

    perda, acuracia = modelo.evaluate(x_teste, y_teste, verbose=0)
    print(f"\nAcurácia no teste: {acuracia:.4f}  |  Perda: {perda:.4f}")

    plotar_historico(historico)

    modelo.save(CAMINHO_MODELO)
    print(f"Modelo salvo em {CAMINHO_MODELO}")