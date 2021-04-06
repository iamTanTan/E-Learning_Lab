from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required
def profile_detail(request):

    profile = Profile.objects.filter(user = request.user)
    enrolled_courses = request.user.courses.all()

    # request.user.courses.add('f1fc85d1-351e-4bf8-90ab-313367bd1d1c')

    context = {
        'profile': profile,
        'enrolled_courses': enrolled_courses,
    }

    return render(request,"profile_detail.html", context)