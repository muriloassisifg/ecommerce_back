from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Defina a URL do banco de dados
DATABASE_URL = "postgresql://postgres:1234@10.5.10.10/db_ecommerce_murilo"  # Substitua com suas credenciais

# Base para todos os modelos
Base = declarative_base()

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.engine = create_engine(DATABASE_URL)
            cls._instance.SessionLocal = sessionmaker(
                autocommit=False, autoflush=False, bind=cls._instance.engine
            )
            cls._instance.recreate_database()  # Chama a função para recriar as tabelas
        return cls._instance

    def get_session(self) -> Session:
        """Retorna uma sessão como um context manager."""
        return self.SessionLocal()  # Retorna a sessão para ser usada com 'with'

    def recreate_database(self):
        """Apaga todas as tabelas e as recria (DADOS EXISTENTES SERÃO PERDIDOS)."""
        Base.metadata.drop_all(bind=self.engine)  # Apaga todas as tabelas
        Base.metadata.create_all(bind=self.engine)  # Cria todas as tabelas novamente

# Instância Singleton do banco de dados
database = Database()
