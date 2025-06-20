async function carregarRelatorio() {
  try {
    const response = await fetch('http://localhost:3000/api/relatorio');
    if (!response.ok) {
      throw new Error('Erro ao carregar relatório');
    }
    const dados = await response.json();

    document.getElementById('total-refeicoes').textContent = dados.totalRefeicoes;
    document.getElementById('media-calorias').textContent = dados.mediaCalorias;
    document.getElementById('mais-usado').textContent = dados.ingredienteMaisUsado;

    document.getElementById('desperdicio').textContent = dados.desperdicioAlimentar;
    document.getElementById('co2').textContent = dados.co2Salvo;

    const lista = document.getElementById('lista-desperdicio');
    lista.innerHTML = "";
    dados.itensDesperdicio.forEach(item => {
      const li = document.createElement('li');
      li.innerHTML = `${item.nome} <span>${item.quantidade}</span>`;
      lista.appendChild(li);
    });

    document.getElementById('dica').textContent = dados.dicaMes;

  } catch (error) {
    console.error('Erro ao carregar dados:', error);
    alert('Erro ao carregar os dados do relatório.');
  }
}

document.addEventListener('DOMContentLoaded', carregarRelatorio);
