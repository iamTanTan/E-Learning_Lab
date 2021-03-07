from .models import Discussion
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
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
def discussion_detail(request, slug):
    discussion = get_object_or_404(Discussion, slug=slug)

    if (not discussion.exists()):
        return render(request, "not_exists.html", {})


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

    return render(request, 'discussion_detail.html', {'post': discussion,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


