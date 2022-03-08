from django.db import models

# Create your models here.

class Meeting(models.Model):
    id = models.SmallAutoField(primary_key=True)
    channel = models.TextField()
    meeting_title = models.TextField(null=True,blank=True)
    meeting_subject = models.TextField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.meeting_title}"

class Channel(models.Model):
    id = models.SmallAutoField(primary_key=True)
    channel = models.TextField()
    app_id= models.TextField()

    def __str__(self):
        return f"{self.app_id}"

