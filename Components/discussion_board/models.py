from django.db import models
from django.contrib.auth.models import User
from Components.courses.models import Courses


class Discussion(models.Model):
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussion_post")
    slug = models.SlugField(max_length=200, unique=True)
    content = models.CharField(max_length=1000)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title

   

    # def get_absolute_url(self):
    #     from django.urls import reverse

    #     return reverse("discussion_list", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    parent_discussion = models.ForeignKey('Discussion', on_delete=models.CASCADE, to_field='id', related_name="parent_discussion")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.content, self.author)