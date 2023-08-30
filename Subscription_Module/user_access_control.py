class UserAccessControl:
    """
    Manages user access based on their subscription.
    """

    def __init__(self, user_id, subscription_type="Free"):
        self.user_id = user_id
        self.subscription_type = subscription_type
        Database.insert_user(user_id, subscription_type)  # Insert user with their subscription type

    def check_access(self, feature):
        """
        Check if the user has access to a specific feature.
        """
        features_by_subscription = {
            "Free": ["basic_response"],
            "Premium": ["basic_response", "advanced_response"],
            "Business": ["basic_response", "advanced_response", "priority_support"]
        }
        
        return feature in features_by_subscription.get(self.subscription_type, [])

    def change_subscription(self, new_subscription_type):
        """
        Update the user's subscription type.
        """
        self.subscription_type = new_subscription_type
        Database.update_subscription(self.user_id, new_subscription_type)  # Update subscription in mock database
        print(f"Subscription updated to {new_subscription_type} for user {self.user_id}.")
