const planner = document.getElementById("planner");
const dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];
const refeicoes = ['Café da manhã', 'Almoço', 'Jantar'];

let receitas = [];
let selectedDay = null;
let selectedMeal = null;
let selectedBlock = null;

function obterToken() {
  const token = localStorage.getItem('token');
  if (!token) {
    alert('Você precisa estar logado!');
    window.location.href = '../Login-e-registro/index.html';
  }
  return token;
}

async function carregarReceitas() {
  const token = obterToken();
  try {
    const response = await fetch('http://localhost:5000/recipes', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error('Erro ao carregar as receitas');
    }

    receitas = await response.json();
    renderizarModalReceitas();
  } catch (error) {
    console.error('Erro:', error);
    alert('Erro ao carregar receitas.');
  }
}

function renderizarModalReceitas() {
  const container = document.getElementById("modal-receitas-list");
  container.innerHTML = "";

  if (receitas.length === 0) {
    container.innerHTML = "<p>Nenhuma receita encontrada.</p>";
    return;
  }

  receitas.forEach(r => {
    const card = document.createElement("div");
    card.classList.add("card-receita");
    card.innerHTML = `
      <h4>${r.nome}</h4>
      <div>${r.tipo_refeicao || ''} • ${r.impacto_ambiental || ''}</div>
    `;
    card.onclick = () => {
      selectedBlock.querySelector(".drop-zone").textContent = r.nome;
      salvarReceitaPlanejada(r);
      fecharModal();
    };
    container.appendChild(card);
  });
}

function abrirModal(day, meal, block) {
  selectedDay = day;
  selectedMeal = meal;
  selectedBlock = block;
  document.getElementById("modal").style.display = "block";
  carregarReceitas();
}

function fecharModal() {
  document.getElementById("modal").style.display = "none";
}

async function salvarReceitaPlanejada(receita) {
  const token = obterToken();
  try {
    await fetch('http://localhost:5000/profile/saved_recipes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        receita_id: receita.id,
        dia: selectedDay,
        refeicao: selectedMeal
      })
    });
  } catch (error) {
    console.error('Erro ao salvar receita planejada:', error);
  }
}

dias.forEach(dia => {
  const column = document.createElement("div");
  column.classList.add("day-column");

  const heading = document.createElement("h3");
  heading.textContent = dia;
  column.appendChild(heading);

  refeicoes.forEach(refeicao => {
    const block = document.createElement("div");
    block.classList.add("meal-block");

    block.onclick = () => abrirModal(dia, refeicao, block);

    const title = document.createElement("h4");
    title.textContent = refeicao;
    const zone = document.createElement("div");
    zone.classList.add("drop-zone");
    zone.textContent = "Clique para escolher";

    const plus = document.createElement("div");
    plus.classList.add("add-button");
    plus.textContent = "+";

    block.appendChild(title);
    block.appendChild(zone);
    block.appendChild(plus);
    column.appendChild(block);
  });

  planner.appendChild(column);
});

window.onclick = function(event) {
  const modal = document.getElementById("modal");
  if (event.target == modal) {
    fecharModal();
  }
};
