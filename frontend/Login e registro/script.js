async function fazerLogin() {
  const email = document.getElementById('login-email').value;
  const senha = document.getElementById('login-senha').value;

  const dadosLogin = { email, senha };

  try {
    const response = await fetch('http://localhost:3000/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dadosLogin)
    });

    if (!response.ok) {
      throw new Error('Falha no login');
    }

    const resultado = await response.json();
    console.log('Login bem-sucedido:', resultado);
    alert('Login realizado com sucesso!');
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

  const dadosRegistro = { nome, email, senha };

  try {
    const response = await fetch('http://localhost:3000/api/usuarios', {
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
