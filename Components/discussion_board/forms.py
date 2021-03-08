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

    def save(self,*args,**kwargs):
        return CommentManager.create_comment(self.request.content, self.request.user)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply',)

    def save(self, new_data):
        return Reply.objects.create_reply(new_data['reply'], self.request.user)
