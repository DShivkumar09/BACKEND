from django.db import models

# Create your models here.

class Feedback(models.Model):
    email =models.EmailField()
    response = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add = True)


