class UserManagement:
    """
    Provides tools to manage users.
    """

    # Simulating a basic database using a dictionary
    user_database = {}
    user_history = {}

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.status = "Active"  # Default status
        # Adding user to our simulated database upon initialization with default status
        UserManagement.user_database[self.user_id] = {"status": self.status, "username": self.username, "email": self.email}
        UserManagement.user_history[self.user_id] = []

    def log_history(self, action):
        """
        Record a user action in the history.
        """
        UserManagement.user_history[self.user_id].append(action)

    def notify_user(self, message):
        """
        Simulate notifying the user.
        """
        print(f"Notification to {self.email}: {message}")

    def ban_user(self):
        """
        Ban a user.
        """
        try:
            self.status = "Banned"
            # Updating the user status in our simulated database
            UserManagement.user_database[self.user_id]["status"] = self.status
            self.log_history("Banned")
            self.notify_user("You have been banned from the platform.")
        except KeyError:
            print("Error: User not found in the database.")

    def mute_user(self):
        """
        Mute a user.
        """
        try:
            self.status = "Muted"
            # Updating the user status in our simulated database
            UserManagement.user_database[self.user_id]["status"] = self.status
            self.log_history("Muted")
            self.notify_user("You have been muted on the platform.")
        except KeyError:
            print("Error: User not found in the database.")

    def activate_user(self):
        """
        Activate a user.
        """
        try:
            self.status = "Active"
            # Updating the user status in our simulated database
            UserManagement.user_database[self.user_id]["status"] = self.status
            self.log_history("Activated")
            self.notify_user("Your account has been activated.")
        except KeyError:
            print("Error: User not found in the database.")

    def update_profile(self, new_username=None, new_email=None):
        """
        Update user profile details.
        """
        try:
            if new_username:
                self.username = new_username
                UserManagement.user_database[self.user_id]["username"] = self.username
                self.log_history(f"Username changed to {new_username}")
            if new_email:
                self.email = new_email
                UserManagement.user_database[self.user_id]["email"] = self.email
                self.log_history(f"Email changed to {new_email}")
            self.notify_user("Your profile details have been updated.")
        except KeyError:
            print("Error: User not found in the database.")
