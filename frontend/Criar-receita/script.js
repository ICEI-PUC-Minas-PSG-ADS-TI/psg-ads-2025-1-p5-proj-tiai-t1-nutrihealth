function obterToken() {
  return localStorage.getItem('token');
}

async function obterListaDeIngredientes() {
  const token = obterToken();

  if (!token) {
    alert('Sessão expirada. Faça login novamente.');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }

  const response = await fetch('http://localhost:5000/ingredientes', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  });

  if (!response.ok) {
    throw new Error('Erro ao buscar a lista de ingredientes.');
  }

  return await response.json();
}

function getSelectedFilter(label) {
  const filtrosContainers = Array.from(document.querySelectorAll('.filtros-box > div'));
  let selecionado = null;

  filtrosContainers.forEach(container => {
    if (container.innerHTML.includes(label)) {
      const checkedBoxes = container.querySelectorAll('input[type="checkbox"]:checked');
      if (checkedBoxes.length === 1) {
        selecionado = checkedBoxes[0].value;
      }
    }
  });

  return selecionado;
}

async function criarJson() {
  const token = obterToken();

  if (!token) {
    alert('Sessão expirada. Faça login novamente.');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }

  const titulo = document.getElementById('titulo').value.trim();
  const ingredientesText = document.getElementById('ingredientes').value.trim();
  const preparo = document.getElementById('preparo').value.trim();
  const impacto = document.getElementById('impacto').value;

  if (!titulo || !ingredientesText || !preparo || impacto === 'Impacto ambiental') {
    alert("Preencha todos os campos obrigatórios!");
    return;
  }

  const tipoDieta = getSelectedFilter('Tipo de dieta');
  const tipoRefeicao = getSelectedFilter('Tipo de refeição');
  const estiloPreparo = getSelectedFilter('Estilo de preparo');

  if (!tipoDieta || !tipoRefeicao || !estiloPreparo) {
    alert('Selecione UMA opção de cada filtro: tipo de dieta, tipo de refeição e estilo de preparo.');
    return;
  }

  let listaIngredientes = [];
  try {
    const ingredientesCadastrados = await obterListaDeIngredientes();
    const nomesIngredientes = ingredientesText.split('\n').map(n => n.trim()).filter(n => n !== "");

    for (const nomeIng of nomesIngredientes) {
      const ingredienteEncontrado = ingredientesCadastrados.find(ing =>
        ing.nome.trim().toLowerCase() === nomeIng.toLowerCase()
      );

      if (!ingredienteEncontrado) {
        throw new Error(`Ingrediente "${nomeIng}" não encontrado. Cadastre-o antes de criar a receita.`);
      }

      listaIngredientes.push({
        id: ingredienteEncontrado.id,
        nome: ingredienteEncontrado.nome
      });
    }
  } catch (error) {
    alert(error.message);
    return;
  }

  const tempoPreparo = "00:00";

  const dados = {
    nome: titulo,
    descricao: ingredientesText,
    tempo_preparo: tempoPreparo,
    modo_preparo: preparo,
    impacto_ambiental: impacto,
    tipo_dieta: tipoDieta,
    tipo_refeicao: tipoRefeicao,
    estilo_preparo: estiloPreparo,
    ingredientes: listaIngredientes
  };

  console.log('Dados enviados:', JSON.stringify(dados, null, 2));

  fetch('http://localhost:5000/recipes', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(dados)
  })
    .then(response => {
      if (response.ok) {
        alert('Receita salva com sucesso!');
        window.location.href = '../Tela-inicial/index.html';
      } else {
        response.json().then(err => {
          alert('Erro ao salvar a receita: ' + (err.error || 'Erro desconhecido'));
        });
      }
    })
    .catch(error => {
      console.error('Erro na requisição:', error);
      alert('Erro de conexão com o servidor.');
    });
}


document.getElementById('imagem').addEventListener('change', function(e) {
  const fileName = e.target.files[0]?.name || 'Carregar imagem';
  document.getElementById('fileLabel').textContent = fileName;
});

function gerarLista() {
  alert('Lista de itens gerada.');
}
