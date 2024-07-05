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

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField