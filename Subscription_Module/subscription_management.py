import random

class Database:  # Simulating a database using a dictionary
    user_subscriptions = {}
    
    @staticmethod
    def update_subscription(user_id, subscription_type):
        Database.user_subscriptions[user_id] = subscription_type

    @staticmethod
    def get_subscription(user_id):
        return Database.user_subscriptions.get(user_id, None)


class Payment:  # Mock payment processing
    @staticmethod
    def process(subscription_type):
        # Simulating a 90% success rate for payment processing
        success = random.random() < 0.90
        if success:
            print(f"Successfully processed payment for {subscription_type} subscription.")
        else:
            print(f"Payment failed for {subscription_type} subscription.")
        return success


class Subscription:
    """
    Manages subscription details and states.
    """
    SUBSCRIPTION_COSTS = {
        "Free": 0,
        "Premium": 10,
        "Business": 20
    }

    def __init__(self, user_id):
        self.user_id = user_id
        self.subscription_type = "Free"  # Default type

    def upgrade_subscription(self, subscription_type):
        """
        Upgrade the user's subscription.
        """
        cost = self.SUBSCRIPTION_COSTS.get(subscription_type, 0)
        if Payment.process(subscription_type):
            self.subscription_type = subscription_type
            Database.update_subscription(self.user_id, subscription_type)
            print(f"Subscription upgraded to {subscription_type} for user {self.user_id}.")

    def downgrade_subscription(self):
        """
        Downgrade the user's subscription.
        """
        self.subscription_type = "Free"
        Database.update_subscription(self.user_id, "Free")
        print(f"Subscription downgraded to Free for user {self.user_id}.")

