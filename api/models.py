from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    
    
    Title = models.CharField(max_length=100,null=False)
    Post = models.TextField(null=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_owner')
    POST_STATUS_CHOICE = [
        ('draft',"Draft"),
        ('published','Published'),
    ]
    post_status = models.CharField(
        max_length=10,
        choices=POST_STATUS_CHOICE,
        default='Draft'
    )
    post_created = models.DateTimeField(default=timezone.now)
    post_published = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Title
    
    