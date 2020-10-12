from django.db import models

class Article(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null = True)
    good_count = models.IntegerField(default = 0)
    images = models.ImageField(default='', upload_to='', null=True)

    def __str__(self):
        return self.content