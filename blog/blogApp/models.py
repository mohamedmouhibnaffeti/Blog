from django.db import models

class Post(models.Model):
    Status_choices = (
        'published', 'Published', 'draft', 'Draft'
    )
    title = models.CharField(max_length=200)
    