from django.db import models

class Post(models.Model):
    Status_choices = (
        'published', 'Published', 'draft', 'Draft'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status_choices)
    