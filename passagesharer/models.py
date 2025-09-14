from django.db import models
from django.conf import settings

# Create your models here.
class Passage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='passages'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    to_passage = models.ForeignKey(
        Passage,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.CharField(max_length=512)
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviewers",
        null=True
    )
