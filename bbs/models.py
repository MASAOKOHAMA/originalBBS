from django.db import models

class Article(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null = True)
    good_count = models.IntegerField(max_length=200, default = 0)

    def __str__(self):
        return self.content