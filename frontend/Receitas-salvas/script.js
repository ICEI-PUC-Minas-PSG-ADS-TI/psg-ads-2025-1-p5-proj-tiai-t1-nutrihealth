let receitas = [];
let planejamento = [];

async function obterToken() {
  const token = localStorage.getItem('token');
  if (!token) {
    alert('Você precisa estar logado para acessar as receitas!');
    window.location.href = '../Login-e-registro/index.html';
  }
  return token;
}

async function carregarPlanejamento() {
  const token = await obterToken();
  try {
    const response = await fetch('http://localhost:5000/planejamento', {
      method: 'GET',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Erro ao carregar planejamento');
    planejamento = await response.json();
  } catch {
    planejamento = [];
  }
}

async function carregarReceitas() {
  const token = await obterToken();
  try {
    const response = await fetch('http://localhost:5000/recipes', {
      method: 'GET',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!response.ok) throw new Error('Erro ao carregar as receitas');
    receitas = await response.json();
  } catch (error) {
    console.error('Erro ao buscar receitas:', error);
    receitas = [];
  }
}

function filtrarReceitasPlanejadas() {
  const idsPlanejadas = planejamento.map(p => p.receita_id);
  return receitas.filter(r => idsPlanejadas.includes(r.id));
}

async function salvarReceitasIndividualmente(receitasFiltradas) {
  const token = await obterToken();
  for (const receita of receitasFiltradas) {
    try {
      await fetch(`http://localhost:5000/recipes/save/${receita.id}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
    } catch (error) {
      console.error(`Erro ao salvar receita ${receita.id}:`, error);
    }
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
    card.style.cursor = "pointer";
    card.addEventListener("click", () => {
      window.location.href = `../Tela-Receita-Detalhada/index.html?id=${r.id}`;
    });

    card.innerHTML = `
      <div class="recipe-info">
        <h3 class="recipe-title">${r.nome}</h3>
        <span class="environmental-impact"><strong>Impacto ambiental: </strong>${r.impacto_ambiental ?? ''}</span>
      </div>
    `;
    container.appendChild(card);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
  await carregarPlanejamento();
  await carregarReceitas();
  const receitasPlanejadas = filtrarReceitasPlanejadas();
  await salvarReceitasIndividualmente(receitasPlanejadas);
  renderizarReceitas(receitasPlanejadas);
});
