from django.db import models

# Create your models here.
class WhatsApp_message(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number =  models.IntegerField(blank=False)
    type = models.CharField(max_length=30)
    message = models.TextField()
    msg_id = models.CharField( max_length=150)
    timestamp = models.TextField()

    def __str__(self):
        return "%s %s %s" %(self.phone_number, self.message, self.msg_id)