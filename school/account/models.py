from django.db import models


class Invite(models.Model):
    email = models.EmailField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


