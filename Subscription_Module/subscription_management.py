class Subscription:
    """
    Manages subscription details and states.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.subscription_type = "Free"  # Default type

    def upgrade_subscription(self, subscription_type):
        """
        Upgrade the user's subscription.
        """
        self.subscription_type = subscription_type
        # Logic to handle payment and update in database

    def downgrade_subscription(self):
        """
        Downgrade the user's subscription.
        """
        self.subscription_type = "Free"
        # Logic to update in database
