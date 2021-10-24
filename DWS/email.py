from templated_mail.mail import BaseEmailMessage


class DWSEmail(BaseEmailMessage):
    template_name = "email/dws_email.html"
