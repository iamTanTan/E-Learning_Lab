from .models import Comment, CommentManager, Reply, ReplyManager
from django import forms

# class DiscussionForm(forms.ModelForm):
#     class Meta:
#         model = Discussion
#         fields = ('created_by', 'content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply',)
