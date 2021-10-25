from templated_mail.mail import BaseEmailMessage


class DWSEmail(BaseEmailMessage):
    template_name = "emails/dws_email.html"
