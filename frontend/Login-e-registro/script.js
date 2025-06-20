async function fazerLogin() {
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-senha').value;

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

    localStorage.setItem('token', resultado.token);

    alert('Login realizado com sucesso!');

  window.location.href = '../Tela-inicial/index.html';

  } catch (error) {
    console.error('Erro no login:', error);
    alert('Falha ao fazer login. Verifique seu email e senha.');
  }
}


async function fazerRegistro() {
  const nome = document.getElementById('register-nome').value;
  const email = document.getElementById('register-email').value;
  const senha = document.getElementById('register-senha').value;
  const confirmar = document.getElementById('register-confirmar').value;

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
  } catch (error) {
    console.error('Erro no registro:', error);
    alert('Falha ao realizar cadastro.');
  }
}
