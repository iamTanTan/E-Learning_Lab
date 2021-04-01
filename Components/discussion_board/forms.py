from .models import Comment, Reply
from django import forms

# class DiscussionForm(forms.ModelForm):
#     class Meta:
#         model = Discussion
#         fields = ('created_by', 'content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
 
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Write a comment here...', 'rows': 6})
    )

    

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply',)

    reply = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Write a response here...', 'rows': 4})
    )




    
