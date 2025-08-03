from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

# Cria a conexão com o banco de dados
db = create_engine("sqlite:///database/database.db")

# Cria a base do banco de dados
Base = declarative_base()

# Cria as classes/tabelas do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)
    
    
    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


# Pedido

# Itens do pedido

# Executa a ação dos metadados do banco de dados (Cria efetivamente o banco de dados)
