from django.db import models

class Article(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null=True)
    good_count = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)
    images = models.ImageField(default='media', upload_to='', null=True)

    def __str__(self):
        return self.content

class Comment(models.Model):
    text = models.CharField('コメント', max_length=300)
    target = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='紐づく日記')
    created_at = models.DateTimeField(auto_now_add=True)
    article_id = models.IntegerField(default=0)