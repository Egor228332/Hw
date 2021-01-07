from django.db import models

class UserMessage(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    message = models.TextField(max_length=150)
    is_processed = models.BooleanField(default=False)
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name},{self.user_email},{self.message}"
