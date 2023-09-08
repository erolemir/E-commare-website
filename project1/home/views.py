from django.shortcuts import render,redirect
from .models import Setting,ContactFormu,ContactFormMessage
from django.contrib import messages

# Create your views here.

def index(request):
    setting = Setting.objects.get()
    context = {"setting":setting}
    return render(request, "home/index.html", context)


def hakkimizda(request):
    setting = Setting.objects.get()
    context = {"setting":setting}
    return render(request, "home/hakkimizda.html",context)

def referances(request):
    setting = Setting.objects.get()
    context = {"setting":setting}
    return render(request, "home/referances.html",context)

def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() #Form ile bağlantı kurma
            data.name = form.cleaned_data["name"] #formdan bilgi alma
            data.email = form.cleaned_data["email"]
            data.subject = form.cleaned_data["subject"]
            data.message = form.cleaned_data["message"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.save() #Datayı veritabanına kaydet
            messages.success = (request,"Mesajınız Başarıyla Gönderilmiştir.")
            return redirect ('iletisim')
        
    setting = Setting.objects.get()
    form = ContactFormu()
    context = {"setting":setting, "form":form}
    return render (request, 'home/iletisim.html',context)