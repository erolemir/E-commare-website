from django.shortcuts import render
from .models import Setting

# Create your views here.

def index(request):
    setting = Setting.objects.get()
    context = {"setting":setting}
    return render(request, "home/index.html", context)
