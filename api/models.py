from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(blank=True, max_length=50)
    text = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ['-created']
