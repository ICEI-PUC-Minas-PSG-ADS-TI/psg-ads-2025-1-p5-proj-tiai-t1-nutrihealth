let receitas = [];

async function carregarReceitas() {
  try {
    const response = await fetch('http://localhost:3000/api/receitas');
    if (!response.ok) {
      throw new Error('Erro ao carregar as receitas');
    }
    const dados = await response.json();
    receitas = dados;
    renderizarReceitas(receitas);
  } catch (error) {
    console.error('Erro ao buscar receitas:', error);
    const container = document.getElementById("recipes-list");
    container.innerHTML = "<p>Erro ao carregar receitas.</p>";
  }
}

function renderizarReceitas(lista) {
  const container = document.getElementById("recipes-list");
  container.innerHTML = "";

  if (lista.length === 0) {
    container.innerHTML = "<p>Nenhuma receita encontrada.</p>";
    return;
  }

  lista.forEach(r => {
    const card = document.createElement("div");
    card.classList.add("recipe-card");
    card.innerHTML = `
      <img src="${r.imagem}" alt="${r.titulo}" class="recipe-image" />
      <h3>${r.titulo}</h3>
    `;
    container.appendChild(card);
  });
}

function obterFiltrosSelecionados() {
  const filtros = {
    dieta: [],
    refeicao: [],
    preparo: []
  };

  document.querySelectorAll("input[name='dieta']:checked").forEach(cb => filtros.dieta.push(cb.value));
  document.querySelectorAll("input[name='refeicao']:checked").forEach(cb => filtros.refeicao.push(cb.value));
  document.querySelectorAll("input[name='preparo']:checked").forEach(cb => filtros.preparo.push(cb.value));

  return filtros;
}

function aplicarFiltros() {
  const { dieta, refeicao, preparo } = obterFiltrosSelecionados();

  const filtradas = receitas.filter(r =>
    (dieta.length === 0 || dieta.includes(r.dieta)) &&
    (refeicao.length === 0 || refeicao.includes(r.refeicao)) &&
    (preparo.length === 0 || preparo.includes(r.preparo))
  );

  renderizarReceitas(filtradas);
}

document.addEventListener("DOMContentLoaded", () => {
  carregarReceitas();
  document.querySelector(".apply-button").addEventListener("click", aplicarFiltros);
});
