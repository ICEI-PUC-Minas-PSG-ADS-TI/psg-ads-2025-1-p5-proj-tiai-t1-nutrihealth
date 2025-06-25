let receitas = [];

async function carregarReceitas() {
  const token = localStorage.getItem('token');

  if (!token) {
    alert('Você precisa estar logado para acessar as receitas!');
    window.location.href = 'login.html';
    return;
  }

  try {
    const response = await fetch('http://localhost:5000/recipes', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error('Erro ao carregar as receitas');
    }

    const dados = await response.json();
    receitas = dados;
    renderizarReceitas(receitas);
  } catch (error) {
    const container = document.getElementById("recipes-list");
    container.innerHTML = "<p>Erro ao carregar receitas</p>";
  }
}

function renderizarReceitas(lista) {
  const container = document.getElementById("recipes-list");
  container.innerHTML = "";

  if (lista.length === 0) {
    container.innerHTML = "<p>Nenhuma receita encontrada</p>";
    return;
  }

  lista.forEach(r => {
    const card = document.createElement("div");
    card.classList.add("recipe-card");
    card.innerHTML = `
      <h3>${r.nome}</h3>
      <p class="impacto"><strong>Impacto ambiental:</strong> ${r.impacto_ambiental}</p>
    `;
    card.addEventListener("click", () => {
      window.location.href = `../Tela-Receita-Detalhada/index.html?id=${r.id}`;
    });
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
  const termoBusca = document.querySelector(".search-bar").value.trim().toLowerCase();

  const filtradas = receitas.filter(r =>
    (dieta.length === 0 || dieta.includes(r.tipo_dieta)) &&
    (refeicao.length === 0 || refeicao.includes(r.tipo_refeicao)) &&
    (preparo.length === 0 || preparo.includes(r.estilo_preparo)) &&
    (termoBusca === "" || r.nome.toLowerCase().includes(termoBusca))
  );

  renderizarReceitas(filtradas);
}


document.addEventListener("DOMContentLoaded", () => {
  carregarNomeUsuario();
  carregarReceitas();
  document.querySelector(".apply-button").addEventListener("click", aplicarFiltros);
  document.querySelector(".search-bar").addEventListener("input", aplicarFiltros);

  const botaoLogout = document.getElementById("logout");
  if (botaoLogout) {
    botaoLogout.addEventListener("click", logout);
  }
});

async function carregarNomeUsuario() {
  const token = localStorage.getItem('token');
  if (!token) return;

  try {
    const response = await fetch('http://localhost:5000/profile', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) throw new Error('Erro ao carregar perfil do usuário');

    const user = await response.json();
    const userGreeting = document.getElementById('user-greeting');
    if (userGreeting && user.name) {
      userGreeting.textContent = `Olá, ${user.name}`;
    }
  } catch (error) {
    console.error(error);
  }
}
