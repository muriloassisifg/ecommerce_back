from models.role_model import Role, RoleCreate
from connection.database import database  # Importe a instância do banco

class RoleRepository:
    
    def get_all(self):
        with database.get_session() as session:
            return session.query(Role).all()

    def get_by_id(self, role_id: int):
        with database.get_session() as session:
            return session.query(Role).filter(Role.id == role_id).first()

    def create(self, role_data: RoleCreate):
        with database.get_session() as session:
            db_role = Role(name=role_data.name)
            session.add(db_role)
            session.commit()
            session.refresh(db_role)
            return db_role

    def delete(self, role_id: int):
        with database.get_session() as session:
            role = session.query(Role).filter(Role.id == role_id).first()
            if role:
                session.delete(role)
                session.commit()
                return True
            return False
