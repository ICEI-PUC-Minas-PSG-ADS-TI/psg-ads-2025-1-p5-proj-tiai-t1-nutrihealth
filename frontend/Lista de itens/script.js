const API_URL = "http://localhost:3000/itens";
let itens = [];
let indexEditar = null;
let idEditar = null;

async function carregarItens() {
  const resposta = await fetch(API_URL);
  itens = await resposta.json();
  renderizarLista();
}

async function salvarItem() {
  const nome = document.getElementById('item-nome').value.trim();
  const quantidade = document.getElementById('item-quantidade').value.trim();

  if (!nome || !quantidade) {
    alert("Preencha todos os campos!");
    return;
  }

  if (idEditar) {
    await fetch(`${API_URL}/${idEditar}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome, quantidade })
    });
  } else {
    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome, quantidade })
    });
  }

  fecharModal();
  await carregarItens();
}

async function deletarItem(id) {
  if (confirm("Deseja deletar este item?")) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    await carregarItens();
  }
}

function editarItem(index) {
  abrirModal(true, index);
}

function abrirModal(editar = false, index = null) {
  const modal = document.getElementById('modal');
  const titulo = document.getElementById('modal-title');
  const inputNome = document.getElementById('item-nome');
  const inputQuantidade = document.getElementById('item-quantidade');

  modal.style.display = 'block';

  if (editar) {
    titulo.textContent = "Editar Item";
    inputNome.value = itens[index].nome;
    inputQuantidade.value = itens[index].quantidade;
    indexEditar = index;
    idEditar = itens[index].id;
  } else {
    titulo.textContent = "Adicionar Item";
    inputNome.value = "";
    inputQuantidade.value = "";
    indexEditar = null;
    idEditar = null;
  }
}

function fecharModal() {
  const modal = document.getElementById('modal');
  modal.style.display = 'none';
}

function renderizarLista() {
  const lista = document.getElementById('lista');
  const busca = document.getElementById('search').value.toLowerCase();

  lista.innerHTML = '';

  const itensFiltrados = itens.filter(item => item.nome.toLowerCase().includes(busca));

  itensFiltrados.forEach((item, index) => {
    const div = document.createElement('div');
    div.className = 'item';

    div.innerHTML = `
      <div class="item-info">
        <div>${item.nome}</div>
        <div>quantidade: ${item.quantidade}</div>
      </div>
      <div class="buttons">
        <button class="edit-button" onclick="editarItem(${index})">Editar</button>
        <button class="delete-button" onclick="deletarItem(${item.id})">Deletar</button>
      </div>
    `;

    lista.appendChild(div);
  });
}

function filtrarItens() {
  renderizarLista();
}

document.addEventListener('DOMContentLoaded', () => {
  carregarItens();
});
