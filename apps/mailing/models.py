from django.db import models


class Mailing(models.Model):
    message_text = models.TextField()
    message_image = models.ImageField(upload_to='mailing_images/', null=True, blank=True,)
    sending_date = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Mailing {self.id} - Sent: {self.is_sent}"

    class Meta:
        db_table = 'mailings'
