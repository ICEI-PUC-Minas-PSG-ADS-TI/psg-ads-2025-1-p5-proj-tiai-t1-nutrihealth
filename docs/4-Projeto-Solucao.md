## 4. Projeto da Solução

## 4.1. Arquitetura da solução

### Arquitetura do Sistema

O diagrama a seguir representa a arquitetura de um sistema web dividido em duas camadas principais: **Client-side (lado do cliente)** e **Servidor-side (lado do servidor)**, conectadas por meio de um **API Gateway**, responsável por intermediar as requisições entre o frontend e o backend.

---

#### 1. Client-side

A camada do cliente é composta por:

- **Frontend HTML**: A interface do usuário é construída em HTML, sendo responsável pela estruturação do conteúdo apresentado ao usuário final.
- **CSS**: Utilizado para estilizar a interface, proporcionando uma experiência visual agradável e responsiva.
- **JavaScript (JS)**: Responsável pela interatividade da aplicação, permitindo a comunicação com o backend por meio de requisições assíncronas (AJAX/fetch), manipulação do DOM, validações, entre outras funcionalidades.

---

#### 2. API Gateway

O **API Gateway** atua como um intermediário que:

- Recebe as requisições do frontend.
- Direciona-as ao backend apropriado.
- Retorna as respostas ao cliente.

Além disso, pode aplicar políticas de segurança, controle de acesso, cache, e registro de logs, centralizando o tráfego entre as camadas.

---

#### 3. Servidor-side

A camada do servidor é composta por:

- **Backend Flask**: Aplicação desenvolvida com o microframework Flask (Python), responsável pela lógica de negócio, manipulação dos dados e respostas às requisições vindas do cliente.
- **Database Postgres**: Banco de dados relacional PostgreSQL utilizado para armazenamento persistente das informações do sistema, como dados de usuários, ingredientes, receitas, listas de compras, entre outros.

---

### Fluxo de Comunicação

1. O usuário interage com a interface HTML.
2. O JavaScript envia requisições HTTP para o API Gateway.
3. O gateway direciona as requisições para o backend Flask.
4. O backend processa os dados, realiza consultas ou atualizações no banco de dados Postgres.
5. O backend retorna a resposta ao gateway, que a envia de volta ao frontend.

---

> Essa arquitetura garante uma separação clara de responsabilidades, facilita a escalabilidade e manutenção do sistema, e proporciona uma base sólida para a adição de novas funcionalidades no futuro.
 
 **Diagrama de Arquitetura**:
 
 ![Diagrama de Arquitetura](./images/Diagrama_Arquitetura.png)
 

### 4.2. Protótipos de telas

https://www.figma.com/design/rVo9G7BQDmsL9HOPxW7OCM/Untitled?node-id=0-1&m=dev&t=pvtHcDxqIq3pgddB-1

A Tela Inicial serve como ponto de entrada e navegação, atendendo aos requisitos de interface intuitiva (RNF-003) e responsividade (RNF-001).

A Tela de Relatório cumpre o RF-002 ao mostrar consumo e desperdício mensal, atendendo à história do usuário que deseja acompanhar seus hábitos alimentares. 

A Tela de Planejamento Semanal atende ao RF-001 e RF-009, permitindo a organização das refeições ao longo da semana, conforme solicitado na história de planejamento da alimentação.

A Tela de Criar Receita contribui para alimentar o sistema com novas opções e possibilita o controle de receitas pelo administrador (RF-004), ligada à história do ADM. 

As Telas de Receita Detalhada (ADM e comum) atendem ao RF-004, RF-006, RF-007 e RF-008, oferecendo visualização completa, impacto ambiental, filtros alimentares e opção de salvar, conforme as histórias de usuário ligadas a personalização e sustentabilidade.

A Tela de Login e Cadastro possibilita o acesso seguro e individual ao sistema, base para todas as histórias de usuários. 

A Lista de Compras cumpre o RF-005 ao gerar listas baseadas nas receitas, ajudando na organização das compras. 

A Lista de Itens realiza o RF-003 ao permitir o cadastro de ingredientes disponíveis, essencial para sugerir receitas com base nos itens em casa (RF-004), ligando a história do usuário que quer evitar desperdícios.

A Tela de Receitas Salvas facilita o acesso a receitas favoritas (RF-008). 

A Tela de Perfil reúne preferências alimentares e atalhos de uso (RF-007, RF-001).

Página Inicial ADM permite a moderação e gestão do conteúdo (RF-010), conforme a história do administrador que deseja manter o sistema organizado.

<img width="576" alt="image" src="https://github.com/user-attachments/assets/08bff154-4039-4d77-ae3c-995b861a7c0b" />
<img width="582" alt="image" src="https://github.com/user-attachments/assets/367b3441-e7a3-4e5c-a7e2-f47d450b59e6" />
<img width="578" alt="image" src="https://github.com/user-attachments/assets/15cdd711-ab05-4143-8337-a203414cee84" />
<img width="580" alt="image" src="https://github.com/user-attachments/assets/6b48e53d-d286-4a2c-a60f-96e555f4d650" />
<img width="578" alt="image" src="https://github.com/user-attachments/assets/a03cdb84-5ccd-49c3-b1f5-1993ad366f2f" />
<img width="575" alt="image" src="https://github.com/user-attachments/assets/9964d71d-1fc6-4450-9918-840212315781" />


## Diagrama de Classes

![image](https://github.com/user-attachments/assets/efdc3960-f007-4b8a-b65a-4ac341b3b2c5)


## Modelo ER

O Modelo ER representa através de um diagrama como as entidades (coisas, objetos) se relacionam entre si na aplicação interativa.]

As referências abaixo irão auxiliá-lo na geração do artefato “Modelo ER”.

> - [Como fazer um diagrama entidade relacionamento | Lucidchart](https://www.lucidchart.com/pages/pt/como-fazer-um-diagrama-entidade-relacionamento)


### 4.3. Modelo de dados

O desenvolvimento da solução proposta requer a existência de bases de dados que permitam efetuar os cadastros de dados e controles associados aos processos identificados, assim como recuperações.
Utilizando a notação do DER (Diagrama Entidade e Relacionamento), elaborem um modelo, na ferramenta visual indicada na disciplina, que contemple todas as entidades e atributos associados às atividades dos processos identificados. Deve ser gerado um único DER que suporte todos os processos escolhidos, visando, assim, uma base de dados integrada. O modelo deve contemplar, também, o controle de acesso de usuários (partes interessadas dos processos) de acordo com os papéis definidos nos modelos do processo de negócio.
_Apresente o modelo de dados por meio de um modelo relacional que contemple todos os conceitos e atributos apresentados na modelagem dos processos._

#### 4.3.1 Modelo ER

O Modelo ER representa através de um diagrama como as entidades (coisas, objetos) se relacionam entre si na aplicação interativa.]

As referências abaixo irão auxiliá-lo na geração do artefato “Modelo ER”.

> - [Como fazer um diagrama entidade relacionamento | Lucidchart](https://www.lucidchart.com/pages/pt/como-fazer-um-diagrama-entidade-relacionamento)

#### 4.3.2 Esquema Relacional

O Esquema Relacional corresponde à representação dos dados em tabelas juntamente com as restrições de integridade e chave primária.
 
As referências abaixo irão auxiliá-lo na geração do artefato “Esquema Relacional”.

> - [Criando um modelo relacional - Documentação da IBM](https://www.ibm.com/docs/pt-br/cognos-analytics/10.2.2?topic=designer-creating-relational-model)

![Exemplo de um modelo relacional](images/modeloRelacional.png "Exemplo de Modelo Relacional.")
---


#### 4.3.3 Modelo Físico

Insira aqui o script de criação das tabelas do banco de dados.

> **OBS:** Se o aluno utilizar BD NoSQL, ele derá incluir o script aqui também. 

Veja um exemplo:

<code>

 -- Criação da tabela Médico
CREATE TABLE Medico (
    MedCodigo INTEGER PRIMARY KEY,
    MedNome VARCHAR(100)
);


-- Criação da tabela Paciente
CREATE TABLE Paciente (
    PacCodigo INTEGER PRIMARY KEY,
    PacNome VARCHAR(100)
);

-- Criação da tabela Consulta
CREATE TABLE Consulta (
    ConCodigo INTEGER PRIMARY KEY,
    MedCodigo INTEGER,
    PacCodigo INTEGER,
    Data DATE,
    FOREIGN KEY (MedCodigo) REFERENCES Medico(MedCodigo),
    FOREIGN KEY (PacCodigo) REFERENCES Paciente(PacCodigo)
);

-- Criação da tabela Medicamento
CREATE TABLE Medicamento (
    MdcCodigo INTEGER PRIMARY KEY,
    MdcNome VARCHAR(100)
);

-- Criação da tabela Prescricao
CREATE TABLE Prescricao (
    ConCodigo INTEGER,
    MdcCodigo INTEGER,
    Posologia VARCHAR(200),
    PRIMARY KEY (ConCodigo, MdcCodigo),
    FOREIGN KEY (ConCodigo) REFERENCES Consulta(ConCodigo),
    FOREIGN KEY (MdcCodigo) REFERENCES Medicamento(MdcCodigo)
);

</code>

Este script deverá ser incluído em um arquivo .sql na pasta src\bd.




### 4.4. Tecnologias


| **Dimensão**   | **Tecnologia**  |
| ---            | ---             |
| SGBD           | PostgreSQL           |
| Front end      | HTML+CSS+JS     |
| Back end       | Flask |
| Deploy         | Github Pages    |



```text
┌──────────────────────────────┐
│     Usuário no Navegador     │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│ Interface Web (HTML/CSS/JS) │
│     hospedada no GitHub     │
│           Pages             │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│      Requisição HTTP         │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│     API Flask (Backend)      │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│     SQLAlchemy (ORM)         │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│ PostgreSQL (Banco de Dados)  │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│  Resposta com dados (JSON)   │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│ JS renderiza os dados na UI  │
└──────────────────────────────┘
```

