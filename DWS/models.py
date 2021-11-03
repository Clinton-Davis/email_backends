from django.db import models


class RecievedEmail(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False)
    type = models.CharField(max_length=250, blank=True)
    time_frame = models.CharField(max_length=250, blank=True)
    goals = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
