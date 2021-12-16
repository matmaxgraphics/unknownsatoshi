from django.core.mail import send_mail






# send mail notification to users and admin after successful registeration
class UserRegisterationNotification():
    def __init__(self, email_subject, email_body, sender_email, receiver_email):

        self.email_subject = email_subject
        self.email_body = email_body
        self.sender_email = sender_email
        self.receiver_email = receiver_email

    def mail_user(self):
        send_mail(
            from_email= self.sender_email,
            subject=self.email_subject,
            message=self.email_body,
            recipient_list= [str(self.receiver_email)],
            fail_silently=False,
        )
        
    def mail_admin(self):
            send_mail(
                from_email= self.sender_email,
                subject=self.email_subject,
                message=self.email_body,
                recipient_list= [str(self.receiver_email)],
                fail_silently=False,
            )


# send mail notification to users and admins after successful subscription
class UserSubscriptionNotification():
    def __init__(self, email_subject, email_body, sender_email, receiver_email):
        self.email_subject = email_subject
        self.email_body = email_body
        self.sender_email = sender_email
        self.receiver_email = receiver_email

    def mail_user(self):
        send_mail(
            from_email= self.sender_email,
            subject=self.email_subject,
            message=self.email_body,
            recipient_list= [str(self.receiver_email)],
            fail_silently=False,
        )
        
    def mail_admin(self):
        send_mail(
            from_email= self.sender_email,
            subject=self.email_subject,
            message=self.email_body,
            recipient_list= [str(self.receiver_email)],
            fail_silently=False,
    )