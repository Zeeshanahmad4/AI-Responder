class UserManagement:
    """
    Provides tools to manage users.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.status = "Active"  # Default status

    def ban_user(self):
        """
        Ban a user.
        """
        self.status = "Banned"
        # Logic to update the user status in the database

    def mute_user(self):
        """
        Mute a user.
        """
        self.status = "Muted"
        # Logic to update the user status in the database

    def activate_user(self):
        """
        Activate a user.
        """
        self.status = "Active"
        # Logic to update the user status in the database
