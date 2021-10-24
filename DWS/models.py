from django.db import models


class RecievedEmail(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=250, blank=True)
    email = models.EmailField(blank=False)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
