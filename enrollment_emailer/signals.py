from django.dispatch import receiver
from common.djangoapps.student.models import EnrollStatusChange
from common.djangoapps.student.signals import ENROLL_STATUS_CHANGE
from edx_ace import ace
from edx_ace.recipient import Recipient
from edx_ace.messages import Inclusion
from edx_ace.message import MessageType
from edx_ace.renderers import EmailRenderer
from edx_ace.policy import ChannelType

class EnrollmentEmail(MessageType):
    def __init__(self, name, base_type='ace_common', fields=None):
        super(EnrollmentEmail, self).__init__(
            name,
            base_type,
            fields,
        )


@receiver(ENROLL_STATUS_CHANGE)
def send_enrollment_email(sender, event=None, user=None, **kwargs):
    if event == EnrollStatusChange.enroll:
        course_id = str(kwargs['course_enrollment'].course.id)
        msg = EnrollmentEmail('enrollment').personalize(
            recipient=Recipient(user.username, user.email),
            language='en',
            user_context={"course_id": course_id},
        )
        ace.send(msg)