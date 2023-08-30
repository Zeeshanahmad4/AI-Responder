import random

class PaymentGateway:
    """
    Mock representation of a payment gateway integration (like Stripe).
    """
    payment_history = {}
    user_balances = {}  # Simulate a user's balance after payment

    @staticmethod
    def make_payment(user_id, amount):
        # Simulating a 90% success rate for payment processing
        success = random.random() < 0.90
        PaymentGateway.payment_history[user_id] = {
            "amount": amount,
            "status": "Success" if success else "Failed"
        }
        
        # If payment succeeds, deduct amount from user balance
        if success:
            PaymentGateway.user_balances[user_id] = PaymentGateway.user_balances.get(user_id, 0) - amount
        
        return success

    @staticmethod
    def refund_payment(user_id, amount):
        print(f"Refunded ${amount} to user {user_id}.")
        PaymentGateway.payment_history[user_id]['status'] = "Refunded"
        # Add the refunded amount back to user balance
        PaymentGateway.user_balances[user_id] = PaymentGateway.user_balances.get(user_id, 0) + amount

    @staticmethod
    def get_payment_history(user_id):
        return PaymentGateway.payment_history.get(user_id, None)


def process_payment(user_id, amount, discount_code=None):
    """
    Process payment for the user.
    """
    # Applying discount
    if discount_code:
        discount_amount = get_discount_amount(discount_code)
        if discount_amount:
            amount -= discount_amount
        else:
            print("Invalid discount code. No discount applied.")

    success = PaymentGateway.make_payment(user_id, amount)

    # Retry logic for failed payment
    if not success:
        print("Initial payment failed. Retrying...")
        success = PaymentGateway.make_payment(user_id, amount)
    
    # Notify user of payment status
    if success:
        print(f"Payment for user {user_id} has been confirmed.")
    else:
        print(f"Payment for user {user_id} failed after retrying. Please try again later.")


def refund(user_id, amount):
    """
    Refund a specific amount to the user.
    """
    # Check if the amount is valid for refund
    if amount > 0:
        PaymentGateway.refund_payment(user_id, amount)
    else:
        print("Invalid refund amount.")


def get_discount_amount(discount_code):
    """
    Get discount amount based on a discount code.
    """
    # Mock discount codes and their values
    discounts = {
        "DISC10": 10,
        "DISC20": 20,
        "DISC30": 30
    }
    return discounts.get(discount_code, 0)

