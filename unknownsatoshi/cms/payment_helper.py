from .models import SubscriptionHistory




def get_subscription_details(user_id, plan_id, amount, email,full_name,phone_no, tx_ref, transaction_id, status):
    print("USER ID IS ", user_id)
    print("PLAN ID in payment_response function IS", plan_id)
    print("EMAIL IS ", email)
    print("FULL NAME IS ", full_name)
    print("PHONE NUMBER IS ", phone_no)

    sub_history = SubscriptionHistory.objects.create(
        user_id=user_id,
        email=email,
        full_name=full_name,
        phone_no=phone_no,
        plan_id=plan_id,
        amount_paid=amount,
        reference=tx_ref, 
        transaction_id=transaction_id, 
        status=status,
        active=True
    )
    print("PLAN SUBSCRIPTION HISTORY DETAILS ARE", sub_history)