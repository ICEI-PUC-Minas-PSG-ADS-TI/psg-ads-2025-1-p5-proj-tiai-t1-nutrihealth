document.getElementById('imagem').addEventListener('change', function(e) {
  const fileName = e.target.files[0]?.name || 'Carregar imagem';
  document.getElementById('fileLabel').textContent = fileName;
});

function gerarLista() {
  alert('Lista de itens gerada.');
}

function criarJson() {
  const titulo = document.getElementById('titulo').value.trim();
  const ingredientes = document.getElementById('ingredientes').value.trim();
  const preparo = document.getElementById('preparo').value.trim();
  const impacto = document.getElementById('impacto').value;
  const imagem = document.getElementById('imagem').files[0]?.name || null;

  const filtros = Array.from(document.querySelectorAll('.filtros input[type="checkbox"]:checked'))
                        .map(el => el.value);

  if (!titulo || !ingredientes || !preparo) {
    alert("Preencha todos os campos obrigatórios!");
    return;
  }

  const dados = {
    titulo,
    ingredientes,
    preparo,
    impactoAmbiental: impacto,
    imagem,
    filtros
  };

  console.log(JSON.stringify(dados, null, 2));


  fetch('http://localhost:3000/api/receitas', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dados)
  })
  .then(response => {
    if (response.ok) {
      alert('Receita salva com sucesso!');
    } else {
      alert('Erro ao salvar.');
    }
  })
  .catch(error => {
    console.error('Erro na requisição:', error);
    alert('Erro de conexão.');
  });
}
