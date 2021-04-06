from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required
def profile_detail(request):

    profile = Profile.objects.filter(user = request.user)

    context = {
        'profile': profile,
    }

    return render(request,"profile_detail.html", context)