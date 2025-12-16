class UserRepository:
    """
    Repository for simulating user data management.
    """

    def __init__(self):
        self.users = [
            {
                'email': 'user@example.com',
                'username': 'testuser',
                'password': 'Password123!',
                'failed_attempts': 0,
                'locked': False
            }
        ]

    def find_by_email(self, email: str) -> dict | None:
        """
        Find a user by email.

        Args:
            email (str): The user's email.

        Returns:
            dict | None: User data if found, None otherwise.
        """
        return next((user for user in self.users if user['email'] == email), None)

    def update_user(self, user: dict):
        """
        Update user information in the database simulation.

        Args:
            user (dict): The user to update.
        """
        for idx, existing_user in enumerate(self.users):
            if existing_user['email'] == user['email']:
                self.users[idx] = user
