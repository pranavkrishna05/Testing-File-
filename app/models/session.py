class Session:
    """
    Represents a session object for tracking user activity.
    """
    def __init__(self, user_id: str, is_active: bool):
        self.user_id = user_id
        self.is_active = is_active