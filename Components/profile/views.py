from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from Components.courses.models import Courses

# Create your views here.
@login_required
def profile_detail(request):
    # Get current user profile 
    profile = Profile.objects.filter(user=request.user)
    
    # Get the enrolled courses list
    enrolled_courses = request.user.courses.all()

    # Get all courses
    courses_list = Courses.objects.all()

    # request.user.courses.add('f1fc85d1-351e-4bf8-90ab-313367bd1d1c')

    context = {
        'profile': profile,
        'enrolled_courses': enrolled_courses,
        'courses_list': courses_list,
    }

    return render(request,"profile_detail.html", context)