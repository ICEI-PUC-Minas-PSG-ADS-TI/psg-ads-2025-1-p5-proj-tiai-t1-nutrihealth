const API_URL = "http://localhost:5000/ingredientes";
let itens = [];
let indexEditar = null;
let idEditar = null;

function obterToken() {
  const token = localStorage.getItem("token");
  if (!token) {
    alert("Sessão expirada. Faça login novamente.");
    window.location.href = "../Login-e-registro/index.html";
  }
  return token;
}

async function carregarItens() {
  const resposta = await fetch(API_URL, {
    headers: {
      "Authorization": `Bearer ${obterToken()}`
    }
  });

  if (!resposta.ok) {
    alert("Erro ao carregar ingredientes. Verifique sua sessão.");
    return;
  }

  itens = await resposta.json();
  renderizarLista();
}

async function salvarItem() {
  const nome = document.getElementById('item-nome').value.trim();
  const quantidade = parseFloat(document.getElementById('item-quantidade').value.trim());
  const unidade = document.getElementById('item-unidade').value.trim();
  const impacto = document.getElementById('item-impacto').value;

  if (!nome || isNaN(quantidade) || !unidade || impacto === "Selecione") {
    alert("Preencha todos os campos!");
    return;
  }

  const ingrediente = {
    nome,
    quantidade,
    unidade_de_medida: unidade,
    impacto_ambiental: impacto
  };

  const metodo = idEditar ? "PUT" : "POST";
  const url = idEditar ? `${API_URL}/${idEditar}` : API_URL;

  try {
    const resposta = await fetch(url, {
      method: metodo,
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${obterToken()}`
      },
      body: JSON.stringify(ingrediente)
    });

    if (!resposta.ok) {
      throw new Error("Erro ao salvar ingrediente.");
    }

    fecharModal();
    await carregarItens();
  } catch (error) {
    console.error(error);
    alert("Erro ao salvar o ingrediente.");
  }
}

async function deletarItem(id) {
  if (confirm("Deseja deletar este ingrediente?")) {
    await fetch(`${API_URL}/${id}`, {
      method: "DELETE",
      headers: {
        "Authorization": `Bearer ${obterToken()}`
      }
    });
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
  const inputUnidade = document.getElementById('item-unidade');
  const selectImpacto = document.getElementById('item-impacto');

  modal.style.display = 'block';

  if (editar) {
    const item = itens[index];
    titulo.textContent = "Editar Ingrediente";
    inputNome.value = item.nome;
    inputQuantidade.value = item.quantidade;
    inputUnidade.value = item.unidade_de_medida;
    selectImpacto.value = item.impacto_ambiental;
    indexEditar = index;
    idEditar = item.id;
  } else {
    titulo.textContent = "Adicionar Ingrediente";
    inputNome.value = "";
    inputQuantidade.value = "";
    inputUnidade.value = "";
    selectImpacto.selectedIndex = 0;
    indexEditar = null;
    idEditar = null;
  }
}

function fecharModal() {
  document.getElementById('modal').style.display = 'none';
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
        <div><strong>${item.nome}</strong></div>
        <div>Quantidade: ${item.quantidade} ${item.unidade_de_medida}</div>
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
