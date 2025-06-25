CREATE TABLE Ingrediente (
    id_ingrediente INT PRIMARY KEY,
    nome VARCHAR(100),
    quantidade FLOAT,
    unidadeDeMedida VARCHAR(50),
    impactoAmbiental FLOAT
);

CREATE TABLE Receita (
    id_receita INT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    impacto_ambiental TEXT,
    tipo_dieta TEXT,
    tipo_refeicao TEXT,
    estilo_preparo TEXT,
    modo_preparo TEXT,
    tempoPreparo DATETIME
);

CREATE TABLE Receita_Ingrediente (
    id_receita INT,
    id_ingrediente INT,
    PRIMARY KEY (id_receita, id_ingrediente),
    FOREIGN KEY (id_receita) REFERENCES Receita(id_receita),
    FOREIGN KEY (id_ingrediente) REFERENCES Ingrediente(id_ingrediente)
);

CREATE TABLE ListaCompras (
    id_lista INT PRIMARY KEY,
    valor FLOAT
);

CREATE TABLE ListaCompras_Ingrediente (
    id_lista INT,
    id_ingrediente INT,
    PRIMARY KEY (id_lista, id_ingrediente),
    FOREIGN KEY (id_lista) REFERENCES ListaCompras(id_lista),
    FOREIGN KEY (id_ingrediente) REFERENCES Ingrediente(id_ingrediente)
);

CREATE TABLE Usuario (
    usuario VARCHAR(18) PRIMARY KEY,
    senha VARCHAR(18),
    tipo ENUM('Cliente', 'Nutricionista')
);

CREATE TABLE Receita_Usuario (
    id_receita INT,
    usuario VARCHAR(18),
    PRIMARY KEY (id_receita, usuario),
    FOREIGN KEY (id_receita) REFERENCES Receita(id_receita),
    FOREIGN KEY (usuario) REFERENCES Usuario(usuario)
);

CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY,
    idade INT,
    nome VARCHAR(50),
    preferencias TEXT,
    usuario VARCHAR(18),
    FOREIGN KEY (usuario) REFERENCES Usuario(usuario)
);

CREATE TABLE Nutricionista (
    id_nutri INT PRIMARY KEY,
    nome VARCHAR(50),
    usuario VARCHAR(18),
    FOREIGN KEY (usuario) REFERENCES Usuario(usuario)
);

CREATE TABLE Nutricionista_Cliente (
    id_nutri INT,
    id_cliente INT,
    PRIMARY KEY (id_nutri, id_cliente),
    FOREIGN KEY (id_nutri) REFERENCES Nutricionista(id_nutri),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE Dashboard (
    id_dashboard INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    mes VARCHAR(10),
    total_refeicoes INT,
    media_calorias_dia FLOAT,
    alimento_mais_usado VARCHAR(100),
    desperdicio_alimentar VARCHAR(20),
    co2_salvo VARCHAR(20),
    itens_mais_desperdicados TEXT,
    dica_do_mes TEXT,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario)
);
