from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import CommentForm,Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.



@login_required(login_url='/login')
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER') #get last url
    if request.method=='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            current_user = request.user
            
            data= Comment()
            data.user_id= current_user.id
            data.product_id= id
            data.subject= form.cleaned_data['subject']
            data.comment= form.cleaned_data['comment']
            data.rate= form.cleaned_data['rate']
            data.ip= request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Yorumunuz başarıyla gönderilmiştir. Teşekkür ederiz.")
            
            return HttpResponseRedirect(url)
    messages.warning(request,"Yorumunuz Gönderilememiştir. Lütfen Kontrol Ediniz.")
    return HttpResponseRedirect(url)