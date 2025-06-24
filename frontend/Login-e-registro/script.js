async function fazerLogin() {
  const emailInput = document.getElementById('login-email');
  const senhaInput = document.getElementById('login-senha');

  const email = emailInput.value;
  const password = senhaInput.value;

  const dadosLogin = { email, password };

  try {
    const response = await fetch('http://localhost:5000/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosLogin)
    });

    if (!response.ok) {
      throw new Error('Falha no login');
    }

    const resultado = await response.json();
    console.log('Login bem-sucedido:', resultado);

    localStorage.setItem('token', resultado.access_token);

    alert('Login realizado com sucesso!');
    window.location.href = '../Tela-inicial/index.html';

  } catch (error) {
    console.error('Erro no login:', error);
    alert('Falha ao fazer login. Verifique seu email e senha.');

    senhaInput.value = '';
  }
}

async function fazerRegistro() {
  const nomeInput = document.getElementById('register-nome');
  const emailInput = document.getElementById('register-email');
  const senhaInput = document.getElementById('register-senha');
  const confirmarInput = document.getElementById('register-confirmar');

  const nome = nomeInput.value;
  const email = emailInput.value;
  const senha = senhaInput.value;
  const confirmar = confirmarInput.value;

  if (senha !== confirmar) {
    alert('As senhas não coincidem!');
    return;
  }

  const dadosRegistro = {
    name: nome,
    email: email,
    password: senha,
    tipo: "Cliente"
  };

  try {
    const response = await fetch('http://localhost:5000/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosRegistro)
    });

    if (!response.ok) {
      throw new Error('Falha no registro');
    }

    const resultado = await response.json();
    console.log('Registro bem-sucedido:', resultado);
    alert('Cadastro realizado com sucesso!');

    // 💡 Aqui limpa os campos
    nomeInput.value = '';
    emailInput.value = '';
    senhaInput.value = '';
    confirmarInput.value = '';

  } catch (error) {
    console.error('Erro no registro:', error);
    alert('Falha ao realizar cadastro.');
  }
}

function mostrarLogin() {
      document.getElementById('login-box').classList.add('active');
      document.getElementById('registro-box').classList.remove('active');
    }

    function mostrarRegistro() {
      document.getElementById('registro-box').classList.add('active');
      document.getElementById('login-box').classList.remove('active');
    }
