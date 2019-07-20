from django.db import models

class AddWord(models.Model):
    word_text=models.CharField(max_length=140)
    date_time=models.DateTimeField('Save Date')
