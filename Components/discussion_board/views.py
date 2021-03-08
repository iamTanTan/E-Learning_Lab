from .models import Discussion
from .forms import CommentForm, ReplyForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def discussions(request, id_field):
    discussions = Discussion.objects.all().filter(courses = (str)(id_field) )
    # detail = discussions.get()
  
    if (not discussions.exists()):
        return render(request, "not_exists.html", {})

    context = {
        "discussions": discussions,
     
    }

    return render(request, "discussions.html", context)


@login_required
def discussion_detail(request, id_field, pk):
    # Retrieve current discussion and the comments that are linked
    discussions = Discussion.objects.all().filter(courses = (str)(id_field) )

    if (not discussions.exists()):
        return render(request, "not_exists.html", {})

    discussion = discussions.get(pk=pk)

    comments = discussion.comments.all()

    # New Comment POST Form
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current user and current discussion board to new comment
            new_comment.created_by = request.user
            new_comment.parent_discussion = discussion
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    comment = comments.get(pk=pk)

    # New Reply POST Form
    new_reply = None
    
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            # Create Comment object but don't save to database yet
            new_reply = reply_form.save(commit=False)
            # Assign the current user and current discussion board to new reply
            new_reply.created_by = request.user
            new_reply.comment = comment
            # Save the reply to the database
            new_reply.save()

    else:
        reply_form = ReplyForm()

    return render(request, 'discussion_detail.html', {'discussion': discussion,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'new_reply': new_reply,
                                           'reply_form': reply_form})