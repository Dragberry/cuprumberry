import logging
import threading

from django.core.mail import send_mail
from django.utils.html import strip_tags

logger = logging.getLogger('django')


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        try:
            send_mail(
                subject=self.subject,
                message=strip_tags(self.html_content),
                html_message=self.html_content,
                from_email='cuprumberry@gmail.com',
                recipient_list=self.recipient_list
            )
        except Exception as e:
            print(e)
            logger.exception(f'An error has occurred while sending email: {str(e)}')


def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()
