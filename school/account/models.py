from django.db import models


class Invite(models.Model):
    email = models.EmailField(unique=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    reg_token = models.TextField(max_length=50, default="")
    reg_token_valid = models.BooleanField(default=True)

#reg_token_valid will be set to True, after account creation or/if few days pass by

#token is  generated for each email for registration purposes

    def __str__(self):
        return self.email


class CsvFile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email
