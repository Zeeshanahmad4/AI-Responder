class UserWorkflow:
    """
    Manages workflows related to user activities.
    """

    def __init__(self, user_id, subscription_type="Free"):
        self.user_id = user_id
        self.subscription_type = subscription_type
        self.history = []  # To track user actions

    def log_history(self, action):
        """
        Record a user action in the history.
        """
        self.history.append((action, self.subscription_type))

    def notify_user(self, message):
        """
        Simulate notifying the user.
        """
        print(f"Notification to {self.user_id}: {message}")

    def renew_subscription(self):
        """
        Renew the user's subscription.
        """
        try:
            # Simulate payment processing
            print(f"Processing payment for {self.user_id}'s {self.subscription_type} subscription renewal...")
            # Assuming payment is successful
            self.log_history("Renewed subscription")
            self.notify_user(f"Your {self.subscription_type} subscription has been renewed!")
        except Exception as e:
            print(f"Error renewing subscription: {e}")

    def upgrade_subscription(self, new_subscription_type):
        """
        Upgrade the user's subscription.
        """
        try:
            # Simulate payment for upgrade
            print(f"Processing payment for upgrading {self.user_id} from {self.subscription_type} to {new_subscription_type}...")
            self.subscription_type = new_subscription_type
            self.log_history(f"Upgraded to {new_subscription_type}")
            self.notify_user(f"Your subscription has been upgraded to {new_subscription_type}!")
        except Exception as e:
            print(f"Error upgrading subscription: {e}")

    def downgrade_subscription(self, new_subscription_type):
        """
        Downgrade the user's subscription.
        """
        try:
            # Simulate processing for downgrade
            print(f"Processing potential refund for downgrading {self.user_id} from {self.subscription_type} to {new_subscription_type}...")
            self.subscription_type = new_subscription_type
            self.log_history(f"Downgraded to {new_subscription_type}")
            self.notify_user(f"Your subscription has been downgraded to {new_subscription_type}!")
        except Exception as e:
            print(f"Error downgrading subscription: {e}")

    def cancel_subscription(self):
        """
        Cancel the user's subscription.
        """
        try:
            # Simulate processing for cancellation
            print(f"Processing cancellation of {self.user_id}'s subscription...")
            self.subscription_type = "Cancelled"
            self.log_history("Cancelled subscription")
            self.notify_user("Your subscription has been cancelled!")
        except Exception as e:
            print(f"Error cancelling subscription: {e}")

    def view_history(self):
        """
        View the history of subscription changes.
        """
        return self.history
