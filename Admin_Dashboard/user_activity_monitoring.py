class UserActivity:
    """
    Monitors and provides details about user activities.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        # Sample data structure to store user activities.
        self.activities = []

    def log_activity(self, activity):
        """
        Log a new user activity.
        """
        self.activities.append(activity)

    def get_recent_activities(self, count=10):
        """
        Fetch the most recent activities of the user.
        """
        return self.activities[-count:]

    def get_all_activities(self):
        """
        Return all activities of the user.
        """
        return self.activities
