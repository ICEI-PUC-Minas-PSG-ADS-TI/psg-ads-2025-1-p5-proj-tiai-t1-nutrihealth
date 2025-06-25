function obterToken() {
  return localStorage.getItem('token');
}

function getQueryParam(param) {
  const params = new URLSearchParams(window.location.search);
  return params.get(param);
}

async function carregarIngredientes() {
  const token = obterToken();
  if (!token) {
    alert('Sessão expirada. Faça login novamente.');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }
  try {
    const res = await fetch('http://localhost:5000/ingredientes', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) throw new Error();
    const ingredientes = await res.json();
    renderizarIngredientes(ingredientes);
  } catch {
    alert('Erro ao carregar ingredientes');
  }
}

function renderizarIngredientes(ingredientes) {
  const container = document.getElementById('ingredientes-container');
  container.innerHTML = '<strong>Ingredientes disponíveis:</strong><br />';
  ingredientes.forEach(ing => {
    const label = document.createElement('label');
    label.innerHTML = `<input type="checkbox" value="${ing.id}" data-nome="${ing.nome}"> ${ing.nome}`;
    container.appendChild(label);
    container.appendChild(document.createElement('br'));
  });
}

async function carregarReceitaPorId(id) {
  const token = obterToken();
  if (!token) {
    alert('Sessão expirada. Faça login novamente.');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }
  try {
    const res = await fetch(`http://localhost:5000/recipes/${id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) throw new Error('Receita não encontrada');
    const receita = await res.json();
    preencherFormulario(receita);
  } catch (e) {
    alert(e.message);
  }
}

function preencherFormulario(receita) {
  document.getElementById('titulo').value = receita.nome || '';
  document.getElementById('preparo').value = receita.modo_preparo || '';
  document.getElementById('impacto').value = receita.impacto_ambiental || '';
  marcarIngredientes(receita.ingredientes);
  preencherCheckboxes('Tipo de dieta:', receita.tipo_dieta);
  preencherCheckboxes('Tipo de refeição:', receita.tipo_refeicao);
  preencherCheckboxes('Estilo de preparo:', receita.estilo_preparo);
}

function marcarIngredientes(ingredientesSelecionados) {
  ingredientesSelecionados.forEach(ing => {
    // Marca pelo id do ingrediente (value do checkbox)
    const checkbox = document.querySelector(`#ingredientes-container input[type="checkbox"][value="${ing.id}"]`);
    if (checkbox) checkbox.checked = true;
  });
}

function preencherCheckboxes(labelTexto, valorSelecionado) {
  const containers = document.querySelectorAll('.filtros-box > div');
  containers.forEach(container => {
    if (container.querySelector('strong')?.textContent === labelTexto) {
      const checkboxes = container.querySelectorAll('input[type="checkbox"]');
      checkboxes.forEach(cb => cb.checked = (cb.value === valorSelecionado));
    }
  });
}

function getSelectedFilter(labelTexto) {
  const containers = document.querySelectorAll('.filtros-box > div');
  for (const container of containers) {
    if (container.querySelector('strong')?.textContent === labelTexto) {
      const checkedBoxes = container.querySelectorAll('input[type="checkbox"]:checked');
      if (checkedBoxes.length === 1) return checkedBoxes[0].value;
    }
  }
  return null;
}

async function criarOuAtualizarReceita(id) {
  const token = obterToken();
  if (!token) {
    alert('Sessão expirada. Faça login novamente.');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }
  const titulo = document.getElementById('titulo').value.trim();
  const preparo = document.getElementById('preparo').value.trim();
  const impacto = document.getElementById('impacto').value;
  if (!titulo || !preparo || impacto === 'Impacto ambiental' || impacto === '') {
    alert('Preencha todos os campos obrigatórios!');
    return;
  }
  const tipoDieta = getSelectedFilter('Tipo de dieta:');
  const tipoRefeicao = getSelectedFilter('Tipo de refeição:');
  const estiloPreparo = getSelectedFilter('Estilo de preparo:');
  if (!tipoDieta || !tipoRefeicao || !estiloPreparo) {
    alert('Selecione UMA opção de cada filtro.');
    return;
  }
  const selecionadosIngredientes = Array.from(document.querySelectorAll('#ingredientes-container input[type="checkbox"]:checked'))
    .map(i => ({ id: parseInt(i.value) }));
  
  const dados = {
    nome: titulo,
    descricao: selecionadosIngredientes.map(i => i.id).join(', '),
    tempo_preparo: "00:00",
    modo_preparo: preparo,
    impacto_ambiental: impacto,
    tipo_dieta: tipoDieta,
    tipo_refeicao: tipoRefeicao,
    estilo_preparo: estiloPreparo,
    ingredientes: selecionadosIngredientes
  };
  const url = id ? `http://localhost:5000/recipes/${id}` : 'http://localhost:5000/recipes';
  const method = id ? 'PUT' : 'POST';
  try {
    const res = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(dados)
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || 'Erro ao salvar receita');
    }
    alert(`Receita ${id ? 'atualizada' : 'criada'} com sucesso!`);
    window.location.href = '../Tela-de-Perfil/index.html';
  } catch (e) {
    alert(e.message);
  }
}

async function excluirReceita(id) {
  const token = obterToken();
  if (!token) {
    alert('Sessão expirada. Faça login novamente.');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }
  if (!confirm('Deseja realmente excluir esta receita?')) return;
  try {
    const res = await fetch(`http://localhost:5000/recipes/${id}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || 'Erro ao excluir receita');
    }
    alert('Receita excluída com sucesso!');
    window.location.href = '../Tela-de-Perfil/index.html';
  } catch (e) {
    alert(e.message);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const id = getQueryParam('id');
  carregarIngredientes();
  if (id) carregarReceitaPorId(id);

  document.getElementById('btn-novo-ingrediente').addEventListener('click', () => {
    abrirModalIngrediente();
  });

  document.querySelector('.create[onclick="criarJson()"]').addEventListener('click', e => {
    e.preventDefault();
    criarOuAtualizarReceita(id);
  });

  document.querySelector('.delete').addEventListener('click', e => {
    e.preventDefault();
    if (id) excluirReceita(id);
  });

  setupModal();
});

function abrirModalIngrediente() {
  document.getElementById('modal-ingrediente').style.display = 'block';
}

function fecharModalIngrediente() {
  document.getElementById('modal-ingrediente').style.display = 'none';
}

function setupModal() {
  document.getElementById('close-modal').addEventListener('click', fecharModalIngrediente);
  document.getElementById('salvar-ingrediente').addEventListener('click', salvarNovoIngrediente);
  window.addEventListener('click', e => {
    if (e.target === document.getElementById('modal-ingrediente')) fecharModalIngrediente();
  });
}

async function salvarNovoIngrediente() {
  const token = obterToken();
  if (!token) {
    alert('Sessão expirada. Faça login novamente.');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }
  const nome = document.getElementById('novo-nome').value.trim();
  const quantidade = document.getElementById('novo-quantidade').value.trim();
  const unidade = document.getElementById('novo-unidade').value.trim();
  const impacto = document.getElementById('novo-impacto').value;
  if (!nome || !quantidade || !unidade || impacto === 'Impacto ambiental' || impacto === '') {
    alert('Preencha todos os campos do novo ingrediente!');
    return;
  }
  const dados = { nome, quantidade, unidade_de_medida: unidade, impacto_ambiental: impacto };
  try {
    const res = await fetch('http://localhost:5000/ingredientes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(dados)
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || 'Erro ao salvar ingrediente');
    }
    alert('Ingrediente criado com sucesso!');
    fecharModalIngrediente();
    await carregarIngredientes();
  } catch (e) {
    alert(e.message);
  }
}
