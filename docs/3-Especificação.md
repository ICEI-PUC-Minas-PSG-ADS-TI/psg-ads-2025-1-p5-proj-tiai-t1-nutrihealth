
# 3. Especificações do Projeto

<span style="color:red">Pré-requisitos: <a href="2-Planejamento-Projeto.md"> Planejamento do Projeto do Software (Cronograma) </a></span>

Nesta parte, será apresentada a definição do problema e a solução do Nosso projeto quando se fala de usuarios. Serão utilizadas técnicas como modelagem de requisitos por meio de histórias de usuários e diagramas UML, além da identificação de critérios de desempenho, segurança e acessibilidade.  

## 3.1 Classificação dos Requisitos Funcionais x Requisitos não Funcionais 

> Com base nas Histórias de Usuário, enumere os requisitos da sua solução. Classifique esses requisitos em dois grupos:

> - **[Requisitos Funcionais (RF)]**(https://pt.wikipedia.org/wiki/Requisito_funcional): correspondem a uma funcionalidade que deve estar presente na
  plataforma (ex: cadastro de usuário).
> - **[Requisitos Não Funcionais (RNF)]**(https://pt.wikipedia.org/wiki/Requisito_n%C3%A3o_funcional):
  correspondem a uma característica técnica, seja de usabilidade, desempenho, confiabilidade, segurança ou outro (ex: suporte a
  dispositivos iOS e Android).

> Lembre-se que cada requisito deve corresponder à uma e somente uma característica alvo da sua solução. Além disso, certifique-se de que
todos os aspectos capturados nas Histórias de Usuário foram cobertos.


### a) Modifique os quadros abaixo, inserindo os Requisitos Funcionais e Não Funcionais do seu projeto. 

Lembre-se de classificá-los de acordo com a prioridade: ALTA, MÉDIA ou BAIXA.

### Requisitos Funcionais


| ID     | Descrição do Requisito                                                        | Prioridade |
|--------|------------------------------------------------------------------------------|------------|
| RF-001 | Permitir que o usuário cadastre tarefas relacionadas ao planejamento de refeições | ALTA       |  
| RF-002 | Emitir um relatório de tarefas no mês, como consumo de alimentos e desperdício | ALTA      |  
| RF-003 | Permitir que o usuário cadastre os ingredientes disponíveis em casa          | ALTA       |  
| RF-004 | Sugerir receitas com base nos ingredientes cadastrados                        | ALTA       |  
| RF-005 | Gerar uma lista de compras personalizada conforme as receitas escolhidas      | MÉDIA      |  
| RF-006 | Indicar o impacto ambiental das receitas sugeridas                            | MÉDIA      |  
| RF-007 | Oferecer filtros para preferências alimentares (vegetariano, vegano, etc.)   | MÉDIA      |  
| RF-008 | Permitir que o usuário salve receitas                                        | BAIXA      |  
| RF-009 | Oferecer um modo de planejamento semanal de refeições                        | MÉDIA      |  
| RF-010 | Permitir compartilhamento de receitas                                       | BAIXA      |  

### Requisitos não Funcionais

| ID      | Descrição do Requisito                                                       | Prioridade |
|---------|-----------------------------------------------------------------------------|------------|
| RNF-001 | O sistema deve ser responsivo para rodar em um dispositivo móvel            | MÉDIA      |
| RNF-002 | Deve processar requisições do usuário em no máximo 3s                       | BAIXA      |
| RNF-003 | A interface deve ser intuitiva                                              | ALTA      |
| RNF-04 | Deve ser compatível com os principais navegadores                            | MÉDIA      |




### b) Modifique o Quadro abaixo e insira as Restrições para o seu projeto.

O projeto está restrito pelos itens apresentados na tabela a seguir.

## Restrições

|ID| Restrição                                               |
|--|---------------------------------------------------------|
|01| O software deve ser compatível com Windows, LINUX E MACOS.     |
|02| O sistema deve ser desenvolvido utilizando Python, PostgreSQL, html, css, js.|
|03| O código-fonte deve ser versionado utilizando Git e hospedado em um repositório privado. |
|04|	A interface deve ser responsiva e adaptável para dispositivos móveis e desktops.| 

**Enumere as restrições à sua solução. Lembre-se de que as restrições geralmente limitam a solução candidata.**

> **Links Úteis**:
> - [O que são Requisitos Funcionais e Requisitos Não Funcionais?](https://codificar.com.br/requisitos-funcionais-nao-funcionais/)
> - [O que são requisitos funcionais e requisitos não funcionais?](https://analisederequisitos.com.br/requisitos-funcionais-e-requisitos-nao-funcionais-o-que-sao/)



## 3.2 Histórias de Usuários
> Apresente aqui as histórias de usuário que são RELEVANTES para o projeto de sua solução. É esperado que haja pelo menos 10 histórias de usuário, dependendo do projeto escolhido para desenvolver.

**OBS:** Se possível, agrupe as histórias de usuário por contexto, para facilitar consultas recorrentes à essa parte do documento.

### a) Modifique o Quadro abaixo e insira as histórias de usuários para o seu projeto.

|EU COMO... `PERSONA`| QUERO/PRECISO ... `FUNCIONALIDADE` |PARA ... `MOTIVO/VALOR`                 |
|--------------------|------------------------------------|----------------------------------------|
|Usuário do sistema  | Registrar minhas tarefas           | Não esquecer de fazê-las               |
|Administrador       | Alterar permissões                 | Permitir que possam administrar contas |
|  xxxx              | Registrar minhas tarefas           | Não esquecer de fazê-las               |
|  yyy               | Alterar permissões                 | Permitir que possam administrar contas |




> **Links Úteis**:
> - [Histórias de usuários com exemplos e template](https://www.atlassian.com/br/agile/project-management/user-stories)
> - [Como escrever boas histórias de usuário (User Stories)](https://medium.com/vertice/como-escrever-boas-users-stories-hist%C3%B3rias-de-usu%C3%A1rios-b29c75043fac)
> - [User Stories: requisitos que humanos entendem](https://www.luiztools.com.br/post/user-stories-descricao-de-requisitos-que-humanos-entendem/)
> - [Histórias de Usuários: mais exemplos](https://www.reqview.com/doc/user-stories-example.html)
> - [9 Common User Story Mistakes](https://airfocus.com/blog/user-story-mistakes/)


-------------------------------------------------------------------------------------------------------------------------------------------

## Tarefas Técnicas (Tasks)

Cada história do usuário é dividida em tarefas específicas para implementação, confome o exemplo abaixo:

## História de Usuário: 
                     Como cliente, eu quero fazer login no sistema para acessar meu perfil.

## As tarefas técnicas referente a história podem ser:
                   Criar a interface de login: Implementar a página com os campos de nome de usuário e senha.
                   Criar validação de entradas: Implementar a verificação de que o usuário inseriu o nome e a senha corretos.
                   Tratar erros de login: Implementar a lógica que exibe mensagens de erro caso nome e senha incorretos.





> **Links Úteis**:
> - [O que são Requisitos Funcionais e Requisitos Não Funcionais?](https://codificar.com.br/requisitos-funcionais-nao-funcionais/)
> - [O que são requisitos funcionais e requisitos não funcionais?](https://analisederequisitos.com.br/requisitos-funcionais-e-requisitos-nao-funcionais-o-que-sao/)
