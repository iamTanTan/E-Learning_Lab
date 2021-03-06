from .models import Discussion
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

class DiscussionList(ListView):
    queryset = Discussion.objects.order_by('-created_on')
    template_name = 'discussion_index.html'

def discussion_detail(request, slug):
    template_name = 'discussion_detail.html'
    discussion = get_object_or_404(Discussion, slug=slug)
    comments = discussion.comments
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current discussion board to the comment
            new_comment.discussion = discussion
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': discussion,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})