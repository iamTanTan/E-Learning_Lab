from django.db import models
from django.contrib.auth import get_user_model
from Components.courses.models import Courses
from django.urls import reverse
import uuid, datetime

# sets User to the currently active user model
User = get_user_model()

# Defines the model for a Discussion
class Discussion(models.Model):
    courses = models.ForeignKey('courses.Courses',  on_delete=models.CASCADE, to_field= 'id', default="dd390af4-07f1-4597-b48a-f585fd79289d" )
    title = models.CharField(max_length=200, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authors")
    slug = models.SlugField(max_length=200, unique=True)
    content = models.CharField(max_length=1000)
    
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse("discussions", kwargs={'id': self.id}) # new



# Defines the model for a Comment which is the child of a Discussion
class Comment(models.Model):
    parent_discussion = models.ForeignKey('Discussion', on_delete=models.CASCADE, to_field='id', related_name="comments")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    # Defines the save functionality
    def save(self):
        if not self.id:
            self.created_on = datetime.date.today()
        self.updated_on = datetime.date.today()
        super(Comment, self).save()

    def __str__(self):
        return "Comment {} by {}".format(self.content, self.created_by)

# Defines the Manager for the Comment Model
class CommentManager(models.Manager):
    def create_comment(self, parent_discussion, created_by):
        new_comment = self.model(parent_discussion=parent_discussion, created_by=user)
        new_comment.save()
        return new_comment



# Defines the model for a Reply which is the child of a Comment
class Reply(models.Model):
    comment = models.ForeignKey('Comment', related_name='replies',  on_delete=models.CASCADE)
    reply = models.TextField(max_length=1000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    # Defines the save functionality
    def save(self):
        if not self.id:
            self.created_on = datetime.date.today()
        self.updated_on = datetime.date.today()
        super(Reply, self).save()

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Reply {} by {}".format(self.reply, self.created_by)

    @property
    def get_replies(self):
        return self.replies.all()

# Defines the Manager for the Reply Model
class ReplyManager(models.Manager):
    def create_reply(self, Comment, user):
        new_reply = self.model(comment=comment, created_by=user)
        new_reply.save()
        return new_reply