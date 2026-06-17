// ----- Configuração do canvas -----
const quadro = document.getElementById("quadro");
const ctx = quadro.getContext("2d");

// Fundo branco e traço preto e grosso.
ctx.fillStyle = "#ffffff";
ctx.fillRect(0, 0, quadro.width, quadro.height);
ctx.lineWidth = 20;
ctx.lineCap = "round";
ctx.lineJoin = "round";
ctx.strokeStyle = "#000000";

let desenhando = false;

// Converte a posição do mouse/dedo para coordenadas dentro do canvas.
function posicao(evento) {
  const r = quadro.getBoundingClientRect();
  const escalaX = quadro.width / r.width;
  const escalaY = quadro.height / r.height;
  const fonte = evento.touches ? evento.touches[0] : evento;
  return {
    x: (fonte.clientX - r.left) * escalaX,
    y: (fonte.clientY - r.top) * escalaY,
  };
}

function iniciar(evento) {
  desenhando = true;
  const p = posicao(evento);
  ctx.beginPath();
  ctx.moveTo(p.x, p.y);
  evento.preventDefault();
}

function mover(evento) {
  if (!desenhando) return;
  const p = posicao(evento);
  ctx.lineTo(p.x, p.y);
  ctx.stroke();
  evento.preventDefault();
}

function parar() {
  desenhando = false;
}

quadro.addEventListener("mousedown", iniciar);
quadro.addEventListener("mousemove", mover);
quadro.addEventListener("mouseup", parar);
quadro.addEventListener("mouseleave", parar);
quadro.addEventListener("touchstart", iniciar);
quadro.addEventListener("touchmove", mover);
quadro.addEventListener("touchend", parar);

// ----- Botão limpar -----
function limpar() {
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, quadro.width, quadro.height);
  document.getElementById("digito").textContent = "—";
  document.getElementById("confianca").textContent = "aguardando desenho";
}

document.getElementById("limpar").addEventListener("click", limpar);

// ----- Predição -----
async function prever() {
  const imagem = quadro.toDataURL("image/png");

  const resposta = await fetch("/prever", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ imagem }),
  });

  const dados = await resposta.json();

  document.getElementById("digito").textContent = dados.digito;
  document.getElementById("confianca").textContent =
    "confiança: " + Math.round(dados.confianca * 100) + "%";
}

document.getElementById("prever").addEventListener("click", prever);