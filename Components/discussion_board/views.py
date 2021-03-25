from .models import Discussion, Comment, Reply, ReplyManager
from .forms import CommentForm, ReplyForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import datetime

#  View for the 'discussions.html' which displays a list of discussions for a given course id
@login_required
def discussions(request, id_field):
    discussions = Discussion.objects.all().filter(courses = (str)(id_field))
  
    if (not discussions.exists()):
        return render(request, "not_exists.html", {})

    context = {
        "discussions": discussions,     
    }

    return render(request, "discussions.html", context)

# View for the 'discussion_detail.html' displays a particular board (pk) and its comments and replies
@login_required
def discussion_detail(request, id_field, pk):
    # Retrieve current discussion and its specific comments
    discussions = Discussion.objects.all().filter(courses = (str)(id_field) )

    if (not discussions.exists()):
        return render(request, "not_exists.html", {})

    discussion = discussions.get(pk=pk)

    # Retrieve all comments associated with the discussion
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
            # Set form to default state after submit
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()


    # New Reply POST Form 
    new_reply = None
    
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():

            # Get the parent id from the comment that will be replied to
            if(comments.exists()):
                parent_id = request.POST.get('parent_id')
                parent_comment = Comment.objects.get(id=parent_id)
                # Create Reply object but don't save to database yet
                new_reply = reply_form.save(commit=False)
                # Assign the current user and current comment to new reply
                new_reply.comment = parent_comment
                new_reply.created_by = request.user
                # Save the reply to the database
                new_reply.save()
                # Set form to default state after submit
                reply_form = ReplyForm()

    else:
        reply_form = ReplyForm()

    return render(request, 'discussion_detail.html', {'discussion': discussion,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'new_reply': new_reply,
                                           'reply_form': reply_form,
                                            })



@login_required
def delete_own_comment(request, pk):
    # delete_own_comment or flag as removed if replies exist
    deleted_comment = Comment.objects.get(pk=pk)
    discussion = deleted_comment.parent_discussion

    if not deleted_comment.replies.exists():
        deleted_comment.delete()
            
    else:
        deleted_comment.is_removed = True
        deleted_comment.save()

    return redirect(Discussion.get_absolute_url(discussion))
           
    

@login_required
def delete_own_reply(request, pk):
    # get particular reply instance
    deleted_reply = Reply.objects.get(pk=pk)

    # get the parent discussion in order to redirect after deletion
    parent_comment = deleted_reply.comment
    discussion = parent_comment.parent_discussion

    # perform deletion
    deleted_reply.delete()

    return redirect(Discussion.get_absolute_url(discussion))
           

           
@login_required
def update_comment(request, pk):
    # get particular comment instance
    comment = Comment.objects.get(pk=pk)
    discussion = comment.parent_discussion  

    # pass the object as instance in form
    comment_form = CommentForm(request.POST or None, instance = comment)

    # save the updated data from the form
    if comment_form.is_valid(): 
        comment_form.save() 

    return redirect(Discussion.get_absolute_url(discussion))