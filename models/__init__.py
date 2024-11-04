from flask_sqlalchemy import SQLAlchemy

# Cria a instância do SQLAlchemy
db = SQLAlchemy()

# Importa os models após a criação do db
from .produto import Produto
from .usuario import Usuario
from .cliente import Cliente
from .pedido import Pedido
from .detalhePedido import DetalhePedido
from .categoriaProduto import CategoriaProduto
