from django.shortcuts import render,redirect,HttpResponse
from .models import Setting,ContactFormu,ContactFormMessage
from product.models import Product,Category,Images
from django.contrib import messages

# Create your views here.

def index(request):
    setting = Setting.objects.get()
     # ... Outfit kategorisinin ID'sini veya adını bulun
    men_outfit_category = Category.objects.get(title="Men outfit")
    women_outfit_category = Category.objects.get(title="Women Outfit")
    kid_outfit_category = Category.objects.get(title="Kid Outfit")

    
    # ... Outfit kategorisine ait ürünleri çekin
    slider_man = Product.objects.filter(category=men_outfit_category)[:4]
    slider_women = Product.objects.filter(category=women_outfit_category)[:4]
    slider_kid = Product.objects.filter(category=kid_outfit_category)[:4]
    
    #veri çekmek için 

    
    context = {"setting":setting,
               "slider_man":slider_man,
               "slider_women":slider_women,
               "slider_kid":slider_kid,
               }
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

def urunler(request):
    setting = Setting.objects.get()
    urunler = Product.objects.all()
    context = {"setting":setting,
               "urunler":urunler}
    
    return render (request, "home/urunler.html",context)

def urun_detay(request,id):
    urunler = Product.objects.get(pk=id)
    resimler = Images.objects.filter(product_id=id)
    context = {"urunler":urunler,
               "resimler":resimler}
    return render(request, "home/urun_detay.html",context)
    