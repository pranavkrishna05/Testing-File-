from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_user_profile(user_id: int) -> dict:
        user = UserRepository.get_user_by_id(user_id)
        if user: 
            return { 'id': user.id, 'username': user.username, 'email': user.email }
        else:
            raise ValueError('User not found')
