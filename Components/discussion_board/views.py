from .models import Discussion, Comment, Reply, ReplyManager
from .forms import CommentForm, ReplyForm
from django.shortcuts import render, get_object_or_404, redirect
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
                print(parent_id)
        
                parent_comment = Comment.objects.get(id=parent_id)

                # Create Reply object but don't save to database yet
                new_reply = reply_form.save(commit=False)
            
                # Assign the current user and current comment to new reply
                # new_reply.comment = parent_comment
                new_reply.created_by = request.user
                    
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



@login_required
def delete_own_comment(request, id_field, pk):
   
    if comment.created_by == request.user:
        if request.method == "POST":
            comment.is_removed = True
            comment.save()
    return redirect(discussion_detail)
           
    