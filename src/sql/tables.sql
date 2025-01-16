-- Conecte-se ao DuckDB antes de executar este script.

-- Remova todas as tabelas existentes
DROP TABLE IF EXISTS itens_pedido;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS categorias;

-- Criação da tabela de usuários
CREATE TABLE usuarios (
    id_usuario INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    data_criacao DATE,
    _ingestiondatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserção de dados na tabela de usuários
INSERT INTO usuarios (id_usuario, nome, email, data_criacao) VALUES
(1, 'Alice Silva', 'alice.silva@example.com', '2023-01-01'),
(2, 'Bruno Costa', 'bruno.costa@example.com', '2023-02-15'),
(3, 'Carla Mendes', 'carla.mendes@example.com', '2023-03-10');

-- Criação da tabela de produtos
CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY,
    nome_produto TEXT,
    preco DECIMAL(10, 2),
    estoque INTEGER,
    _ingestiondatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserção de dados na tabela de produtos
INSERT INTO produtos (id_produto, nome_produto, preco, estoque) VALUES
(101, 'Notebook', 4500.00, 10),
(102, 'Smartphone', 2500.00, 25),
(103, 'Mouse', 50.00, 100),
(104, 'Teclado', 150.00, 50),
(105, 'Monitor', 1200.00, 15),
(106, 'Cadeira Gamer', 850.00, 20);

-- Adicionando mais registros manualmente na tabela de produtos
INSERT INTO produtos (id_produto, nome_produto, preco, estoque) VALUES
(107, 'Webcam', 300.00, 50),
(108, 'Headset', 250.00, 60),
(109, 'Impressora', 900.00, 20),
(110, 'HD Externo', 500.00, 40),
(111, 'Pendrive', 80.00, 200),
(112, 'Fone Bluetooth', 150.00, 100),
(113, 'Tablet', 1500.00, 30),
(114, 'Smartwatch', 700.00, 25),
(115, 'Cabo HDMI', 30.00, 500),
(116, 'Roteador Wi-Fi', 350.00, 45);

-- Criação da tabela de pedidos
CREATE TABLE pedidos (
    id_pedido INTEGER PRIMARY KEY,
    id_usuario INTEGER,
    data_pedido DATE,
    valor_total DECIMAL(10, 2),
    _ingestiondatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);

-- Inserção de dados na tabela de pedidos
INSERT INTO pedidos (id_pedido, id_usuario, data_pedido, valor_total) VALUES
(1001, 1, '2023-06-01', 4550.00),
(1002, 2, '2023-06-15', 2550.00),
(1003, 3, '2023-07-01', 50.00),
(1004, 1, '2023-08-01', 1350.00),
(1005, 2, '2023-08-10', 2050.00),
(1006, 3, '2023-08-15', 850.00);

-- Adicionando mais registros manualmente na tabela de pedidos
INSERT INTO pedidos (id_pedido, id_usuario, data_pedido, valor_total) VALUES
(1007, 1, '2023-08-20', 150.00),
(1008, 2, '2023-08-22', 3200.00),
(1009, 3, '2023-08-25', 1800.00),
(1010, 1, '2023-08-30', 750.00),
(1011, 2, '2023-09-05', 450.00);

-- Criação da tabela de itens do pedido
CREATE TABLE itens_pedido (
    id_item INTEGER PRIMARY KEY,
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER,
    preco_unitario DECIMAL(10, 2),
    _ingestiondatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
);

-- Inserção de dados na tabela de itens do pedido
INSERT INTO itens_pedido (
    id_item, id_pedido, id_produto, quantidade, preco_unitario
) VALUES
(1, 1001, 101, 1, 4500.00),
(2, 1002, 102, 1, 2500.00),
(3, 1003, 103, 1, 50.00),
(4, 1004, 104, 2, 150.00),
(5, 1005, 105, 1, 1200.00),
(6, 1006, 106, 1, 850.00);

-- Adicionando mais registros manualmente na tabela de itens do pedido
INSERT INTO itens_pedido (
    id_item, id_pedido, id_produto, quantidade, preco_unitario
) VALUES
(7, 1007, 107, 1, 150.00),
(8, 1008, 108, 2, 250.00),
(9, 1009, 109, 1, 900.00),
(10, 1010, 110, 3, 500.00),
(11, 1011, 111, 5, 80.00);

-- Criação da tabela de categorias de produtos
CREATE TABLE categorias (
    id_categoria INTEGER PRIMARY KEY,
    nome_categoria TEXT,
    _ingestiondatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserção de dados na tabela de categorias
INSERT INTO categorias (id_categoria, nome_categoria) VALUES
(1, 'Eletrônicos'),
(2, 'Acessórios'),
(3, 'Informática');
