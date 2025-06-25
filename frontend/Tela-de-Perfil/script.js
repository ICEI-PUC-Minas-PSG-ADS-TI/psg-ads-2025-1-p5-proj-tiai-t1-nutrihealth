let receitas = [];

async function carregarNomeUsuario() {
  const token = localStorage.getItem('token');
  if (!token) return;

  try {
    const response = await fetch('http://localhost:5000/profile', {
      method: 'GET',
      headers: {
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

async function carregarReceitas() {
  const token = localStorage.getItem('token');

  if (!token) {
    alert('Você precisa estar logado para acessar as receitas!');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }

  try {
    const response = await fetch('http://localhost:5000/recipes/user', {
      method: 'GET',
      headers: {
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
    const card = document.createElement("a");
    card.href = `../Criar-receita/index.html?id=${r.id}`;
    card.classList.add("card-receita");

    card.innerHTML = `
      <h3>${r.nome}</h3>
      <p class="impacto">Impacto ambiental: ${r.impacto_ambiental || 'Não informado'}</p>
    `;
    container.appendChild(card);
  });
}


function logout() {
  localStorage.removeItem('token');
  window.location.href = '../Login-e-registro/index.html';
}

document.addEventListener("DOMContentLoaded", () => {
  carregarNomeUsuario();
  carregarReceitas();

  const botaoLogout = document.getElementById("logout");
  if (botaoLogout) {
    botaoLogout.addEventListener("click", logout);
  }
});
