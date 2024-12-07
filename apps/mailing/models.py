from django.db import models


class Mailing(models.Model):
    """
    id: int
    message_text: text
    message_content: List[str]

    sending_date: datetime
    is_delivered: bool
    """
    ...

