from django.db import models
from django.contrib.auth.hashers import make_password

class application(models.Model):
    Username = models.TextField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    password = models.TextField(max_length=100, blank=True)
    phonenumber = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
