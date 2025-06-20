let itens = [];

async function buscarItensDoBanco() {
  try {
    const response = await fetch('http://localhost:3000/api/itens');
    if (!response.ok) throw new Error('Erro ao buscar dados');

    itens = await response.json();
    renderizarLista();
  } catch (error) {
    console.error('Erro ao buscar itens:', error);
    const lista = document.getElementById('lista-itens');
    lista.innerHTML = "<p>Erro ao carregar os itens.</p>";
  }
}

function renderizarLista(filtro = "") {
  const lista = document.getElementById('lista-itens');
  lista.innerHTML = "";

  const itensFiltrados = itens.filter(item => 
    item.nome.toLowerCase().includes(filtro.toLowerCase())
  );

  if (itensFiltrados.length === 0) {
    lista.innerHTML = "<p>Nenhum item encontrado.</p>";
    return;
  }

  itensFiltrados.forEach(item => {
    const div = document.createElement('div');
    div.classList.add('item');
    div.innerHTML = `
      <div class="item-nome">${item.nome}</div>
      <div class="item-quantidade">quantidade: ${item.quantidade}</div>
    `;
    lista.appendChild(div);
  });
}

document.getElementById('search-input').addEventListener('input', (e) => {
  const valor = e.target.value;
  renderizarLista(valor);
});

document.addEventListener('DOMContentLoaded', () => {
  buscarItensDoBanco();
});
