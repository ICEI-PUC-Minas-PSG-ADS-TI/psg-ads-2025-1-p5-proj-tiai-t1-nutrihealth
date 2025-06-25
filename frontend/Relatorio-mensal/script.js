async function obterToken() {
  const token = localStorage.getItem('token');
  if (!token) {
    alert('Sessão expirada. Redirecionando para login...');
    window.location.href = '../Login-e-registro/index.html';
  }
  return token;
}

function formatarMes(mesTexto) {
  const mapaMeses = {
    "Janeiro": "01", "Fevereiro": "02", "Março": "03", "Abril": "04",
    "Maio": "05", "Junho": "06", "Julho": "07", "Agosto": "08",
    "Setembro": "09", "Outubro": "10", "Novembro": "11", "Dezembro": "12"
  };
  
  const [nomeMes, ano] = mesTexto.split(" ");
  const mesNum = mapaMeses[nomeMes];
  return `${mesNum}-${ano}`;
}

async function carregarRelatorio() {
  const token = await obterToken();

  const selectMes = document.getElementById('mes');
  const mesSelecionado = formatarMes(selectMes.value);

  try {
    const response = await fetch(`http://localhost:5000/dashboard?mes=${encodeURIComponent(mesSelecionado)}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error('Erro ao carregar relatório');
    }

    const dados = await response.json();

    document.getElementById('total-refeicoes').textContent = dados.total_refeicoes ?? '--';
    document.getElementById('media-calorias').textContent = dados.media_calorias_dia ?? '--';
    document.getElementById('mais-usado').textContent = dados.alimento_mais_usado ?? '--';

    document.getElementById('desperdicio').textContent = dados.desperdicio_alimentar ?? '--';
    document.getElementById('co2').textContent = dados.co2_salvo ?? '--';

    const lista = document.getElementById('lista-desperdicio');
    lista.innerHTML = "";
    (dados.itens_mais_desperdicados || []).forEach(item => {
      const li = document.createElement('li');
      li.innerHTML = `${item.nome} <span>${item.quantidade}</span>`;
      lista.appendChild(li);
    });

    document.getElementById('dica').textContent = dados.dica_do_mes ?? '--';

  } catch (error) {
    console.error('Erro ao carregar dados:', error);
    alert('Erro ao carregar os dados do relatório.');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  carregarRelatorio();

  const selectMes = document.getElementById('mes');
  selectMes.addEventListener('change', carregarRelatorio);
});
