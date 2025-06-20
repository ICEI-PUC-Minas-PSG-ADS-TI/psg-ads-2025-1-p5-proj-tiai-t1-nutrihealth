async function carregarDetalhesDaReceita() {
  const token = localStorage.getItem('token');

  if (!token) {
    alert('Você precisa estar logado para acessar esta receita!');
    window.location.href = '../Login-e-registro/index.html';
    return;
  }

  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');

  if (!id) {
    alert('ID da receita não encontrado.');
    return;
  }

  try {
    const response = await fetch(`http://localhost:5000/recipes/${id}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error('Erro ao carregar a receita');
    }

    const receita = await response.json();

    document.getElementById("recipe-title").textContent = receita.titulo;
    document.getElementById("recipe-ingredients").innerHTML = receita.ingredientes.replace(/\n/g, "<br>");
    document.getElementById("recipe-steps").innerHTML = receita.modo_preparo.replace(/\n/g, "<br><br>");
    document.getElementById("recipe-image").src = receita.imagem;
    document.getElementById("recipe-image").alt = receita.titulo;

  } catch (error) {
    console.error('Erro ao buscar receita:', error);
    document.querySelector(".container").innerHTML = "<p>Erro ao carregar a receita.</p>";
  }
}

document.addEventListener("DOMContentLoaded", carregarDetalhesDaReceita);
