from django.db import models

class Tips(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='tips', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
