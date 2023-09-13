from django.shortcuts import render,redirect ,HttpResponse
from home.models import UserProfile
from django.contrib import messages

from product.models import Comment
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def profile(request):
    profile = UserProfile.objects.get(user_id=request.user)
    context = {'profile': profile}
    return render(request, 'user/userprofile.html',context)
# Create your views here.

def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Your account has been updated!")
            return redirect('/user')
    else:
        current_user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'user_form':user_form,
                   'profile_form':profile_form}
        return render(request,'user/user_update.html',context)
    
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user) # Important!
            messages.success(request,"Şifreniz Başarıyla Değiştirildi")
            return redirect('index')
        else:
            messages.error(request,"Please correct the error below.<br>"+str(form.errors))
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'user/change_password.html',{'form':form})
    
@login_required(login_url='/login') # Check login
def comments(request):
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'comments':comments}
    return render(request,'user/user_comments.html',context)

@login_required(login_url='/login') # Check login
def deletecomments(request,id):
    current_user = request.user
    Comment.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request,"Yorumunuz Silinmiştir")
    return redirect('/user/comments')