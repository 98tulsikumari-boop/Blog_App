from django.db import models
from app_api_account.models import User
from app_api_category.models import Category
from app_api_tag.models import Tag

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")   
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog_covers/', blank=True, null=True )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="blogs"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="blogs"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Latest first

    def __str__(self):
        return self.title


