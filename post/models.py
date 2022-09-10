from django.db import models
from django.utils.text import slugify

from accounts.models import CustomUser


class CreateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


class Post(CreateTime):
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='feeds')
    title = models.CharField(max_length=256)
    intro = models.TextField()
    body = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    comments = models.ManyToManyField(CustomUser,through='Comment',through_fields=('post' ,'author'), related_name='comments')

    def __str__(self) -> str:
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

class Comment(CreateTime):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='user_comment')
    author = models.ForeignKey(CustomUser, null=True , on_delete= models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text