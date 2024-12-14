from dao.user_dao import UserDAO
from models.user import User  # Certifique-se de importar a classe User do módulo correto

class UserRepository:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def register_user(self, username: str, email: str, hashed_password: str):
        existing_user = self.user_dao.get_by_username(username)
        if existing_user:
            return None  # Indica que o usuário já existe
        
        # Cria um novo objeto User
        user = User(username=username, email=email, password=hashed_password)
        return self.user_dao.create(user)

    def authenticate_user(self, username: str, password: str):
        user = self.user_dao.get_by_username(username)
        if user and user.check_password(password):
            return user
        return None
