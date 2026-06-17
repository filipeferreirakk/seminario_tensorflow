# Reconhecimento de Dígitos Manuscritos com TensorFlow

Projeto de seminário sobre a biblioteca **TensorFlow**. Uma rede neural é
treinada no dataset **MNIST** para reconhecer dígitos de 0 a 9, e uma pequena
aplicação web permite **desenhar um número com o mouse e ver a predição ao vivo**,
com a confiança de cada classe.

> Dica: depois de rodar `python train.py`, você pode tirar um print da
> interface e adicioná-lo aqui para deixar o repositório mais bonito.

## O que o projeto mostra

- Como carregar e pré-processar dados com TensorFlow/Keras
- Como construir, treinar e avaliar uma rede neural
- Como salvar um modelo e usá-lo depois em uma aplicação real
- Uma demonstração interativa que prende a atenção da plateia

## Estrutura

\`\`\`
mnist-tensorflow/
├── train.py            # treina a rede e gera o modelo + gráficos
├── app.py              # servidor Flask com a demonstração ao vivo
├── utils.py            # pré-processamento das imagens
├── templates/
│   └── index.html      # página com o canvas de desenho
├── static/
│   ├── style.css       # estilo da interface
│   └── script.js       # desenho no canvas + chamada de predição
├── requirements.txt
└── README.md
\`\`\`

## Como rodar

1. Crie um ambiente virtual e instale as dependências:

   \`\`\`bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   \`\`\`

2. Treine o modelo (baixa o MNIST automaticamente na primeira vez):

   \`\`\`bash
   python train.py
   \`\`\`

   Isso gera o arquivo \`mnist_model.keras\` e algumas imagens
   (\`amostras.png\`, \`historico.png\`, \`predicoes.png\`, \`matriz_confusao.png\`)
   úteis para a apresentação.

3. Suba a aplicação web:

   \`\`\`bash
   python app.py
   \`\`\`

   Abra <http://127.0.0.1:5000> no navegador, desenhe um dígito e clique em
   **Prever**.

## Como funciona

O modelo é uma rede neural simples: a imagem 28x28 é achatada em um vetor de
784 valores, passa por uma camada densa de 128 neurônios com ativação ReLU
(e um Dropout para reduzir overfitting) e termina em 10 saídas com softmax,
que viram as probabilidades de cada dígito. A maior probabilidade é a resposta.

No app, o desenho do canvas é enviado ao servidor, convertido para tons de
cinza, invertido (dígito branco em fundo preto, como no MNIST), redimensionado
para 28x28 e normalizado — exatamente o formato que o modelo espera.

## Tecnologias

TensorFlow/Keras, Flask, Pillow, Matplotlib e NumPy.