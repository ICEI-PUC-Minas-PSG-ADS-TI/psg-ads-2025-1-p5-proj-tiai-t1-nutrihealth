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
        'Authorization': `Bearer ${token}` // ✅ Crase adicionada aqui
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
    const card = document.createElement("article");
    card.classList.add("recipe-card");
    card.innerHTML = `
      <img class="recipe-image" src="${r.imagem}" alt="${r.titulo}" />
      <div class="recipe-info">
        <h3 class="recipe-title">${r.titulo}</h3>
        <span class="environmental-impact">${r.impacto_ambiental ?? ''}</span>
      </div>
    `;
    container.appendChild(card);
  });
}

function logout() {
  localStorage.removeItem('token');
  window.location.href = 'login.html';
}

document.addEventListener("DOMContentLoaded", () => {
  carregarReceitas();

  const botaoLogout = document.getElementById("logout");
  if (botaoLogout) {
    botaoLogout.addEventListener("click", logout);
  }
});
