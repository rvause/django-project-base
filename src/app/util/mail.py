import threading

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.template import Context
from django.contrib.sites.models import Site


class MessageThread(threading.Thread):

    def __init__(self, msg):
        self.msg = msg
        threading.Thread.__init__(self)

    def run(self):
        self.msg.send(fail_silently=True)


def send_async_email(
    template,
    ctx_dict,
    subject,
    to,
    attachments=[],
    from_email=None
):
    '''Send HTML email in separate thread. Use template and
    context dict provided.

    '''
    site = Site.objects.get_current()
    body = render_to_string(
        template,
        Context(dict(site=site, **ctx_dict))
    )

    msg_kw = dict(
        subject=subject,
        body=body,
        to=to,
    )

    if from_email:
        msg_kw['from_email'] = from_email
    
    msg = EmailMessage(**msg_kw)
    msg.content_subtype = 'html'

    for path in attachments:
        msg.attach_file(path)

    MessageThread(msg).start()

