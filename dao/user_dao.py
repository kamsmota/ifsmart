from models.user import User
from sqlalchemy.orm import Session

class UserDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int):
        return self.session.query(User).filter_by(id=user_id).first()

    def get_by_username(self, username: str):
        return self.session.query(User).filter_by(username=username).first()

    def create(self, user: User):
        self.session.add(user)
        self.session.commit()
        return user
