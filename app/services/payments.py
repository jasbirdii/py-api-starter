
import stripe

from ..config import settings

# Initialize Stripe
if settings.STRIPE_SECRET_KEY:
    stripe.api_key = settings.STRIPE_SECRET_KEY


def create_payment_intent(amount: int, currency: str = "usd", metadata: dict | None = None) -> dict:
    """Create a Stripe payment intent."""
    if not settings.STRIPE_SECRET_KEY:
        raise ValueError("Stripe secret key not configured")

    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            metadata=metadata or {}
        )
        return {
            "client_secret": intent.client_secret,
            "payment_intent_id": intent.id,
            "status": intent.status
        }
    except stripe.error.StripeError as e:
        raise ValueError(f"Stripe error: {str(e)}") from e


def retrieve_payment_intent(payment_intent_id: str) -> dict:
    """Retrieve a Stripe payment intent."""
    if not settings.STRIPE_SECRET_KEY:
        raise ValueError("Stripe secret key not configured")

    try:
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return {
            "id": intent.id,
            "status": intent.status,
            "amount": intent.amount,
            "currency": intent.currency,
            "metadata": intent.metadata
        }
    except stripe.error.StripeError as e:
        raise ValueError(f"Stripe error: {str(e)}") from e


def cancel_payment_intent(payment_intent_id: str) -> dict:
    """Cancel a Stripe payment intent."""
    if not settings.STRIPE_SECRET_KEY:
        raise ValueError("Stripe secret key not configured")

    try:
        intent = stripe.PaymentIntent.cancel(payment_intent_id)
        return {
            "id": intent.id,
            "status": intent.status
        }
    except stripe.error.StripeError as e:
        raise ValueError(f"Stripe error: {str(e)}") from e
