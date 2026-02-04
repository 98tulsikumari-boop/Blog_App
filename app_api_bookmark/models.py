from django.db import models 
from app_api_account.models import User
from app_api_blog.models import Blog


# Create your models here.
class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="bookmarked_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "blog")   # One user can bookmark a blog only once

    def __str__(self):
        return f"{self.user.username} - {self.blog.title}"
