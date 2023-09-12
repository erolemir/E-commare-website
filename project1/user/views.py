from django.shortcuts import render
from home.models import UserProfile


def profile(request):
    profile = UserProfile.objects.get(user_id=request.user)
    context = {'profile': profile}
    return render(request, 'user/userprofile.html',context)
# Create your views here.
