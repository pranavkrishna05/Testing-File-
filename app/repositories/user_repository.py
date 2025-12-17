from app.models.user import User
from app.models import db

class UserRepository:
    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def add_user(user: User) -> None:
        db.session.add(user)
        db.session.commit()
