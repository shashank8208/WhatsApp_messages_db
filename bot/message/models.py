from django.db import models

# Create your models here.
class WhatsApp_message(models.Model):
    id = models.AutoField(primary_key=True)
    wa_id =  models.IntegerField(blank=False)
    msg_type = models.CharField(max_length=30)
    message = models.TextField()
    msg_id = models.CharField( max_length=150)
    timestamp = models.DateTimeField()
    sent = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)