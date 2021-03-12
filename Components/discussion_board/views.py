from .models import Discussion, Comment, Reply, ReplyManager
from .forms import CommentForm, ReplyForm, DeleteCommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def discussions(request, id_field):
    discussions = Discussion.objects.all().filter(courses = (str)(id_field))
  
    if (not discussions.exists()):
        return render(request, "not_exists.html", {})

    context = {
        "discussions": discussions,
     
    }

    return render(request, "discussions.html", context)


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

    # delete_own_comment or flag as removed if replies exist
    deleted_comment = None

    if request.method == "POST":
        delete_comment_form = DeleteCommentForm(request.POST)
        if delete_comment_form.is_valid():
            
            if(comments.exists()):            
                delete_id = request.POST.get('comment_id')
                print(delete_id)
                deleted_comment = Comment.objects.get(id=delete_id)
                deleted_comment = delete_comment_form.save(commit=False)
                deleted_comment.id = delete_id

                if not deleted_comment.replies.exists():
                    deleted_comment.delete()
                    # Must repopulate comments after deletion
                    comments = discussion.comments.all()
                        
                else:
                    deleted_comment.is_removed = True
                    # deleted_comment.created_on = datetime.date.()
                    deleted_comment.save()
    
                delete_comment_form = DeleteCommentForm()
    else:
         delete_comment_form = DeleteCommentForm()


    return render(request, 'discussion_detail.html', {'discussion': discussion,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'new_reply': new_reply,
                                           'reply_form': reply_form,
                                           'delete_comment_form': delete_comment_form,})



@login_required
def delete_own_comment(request):
    if request.method == "POST":
        delete_comment_form = DeleteCommentForm(request.POST)
        if delete_comment_form.is_valid():
            comment_id = request.POST.get(comment_id)
            print(comment_id)
            comment = Comment.objects.get(id=comment_id)
                
            if comment.created_by == request.user:
                            
                if comment.replies.exists():
                    comment.delete()
                else:
                    comment.is_removed = True
                    comment.save()

                delete_comment_form = DeleteCommentForm()
           
    