class SubscriptionOverview:
    """
    Provides an overview of all subscriptions.
    """

    def __init__(self):
        # Sample data structure to store subscription data. 
        # In a real-world scenario, this would be fetched from a database.
        self.subscriptions_data = {
            "Free": [],
            "Premium": [],
            "Business": []
        }

    def get_total_subscriptions(self):
        """
        Return the total number of subscriptions.
        """
        return sum(len(subscribers) for subscribers in self.subscriptions_data.values())

    def get_subscription_counts(self):
        """
        Return the count of each subscription type.
        """
        return {tier: len(subscribers) for tier, subscribers in self.subscriptions_data.items()}

    def get_subscription_details(self, subscription_type):
        """
        Return details of subscribers for a specific subscription type.
        """
        return self.subscriptions_data.get(subscription_type, [])
