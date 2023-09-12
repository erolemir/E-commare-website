import json
from django.shortcuts import render,redirect,HttpResponse , HttpResponseRedirect
from order.models import ShopCard
from .models import Setting,ContactFormu,ContactFormMessage , UserProfile
from product.models import Product,Category,Images,Comment
from django.contrib import messages
from product.views import addcomment
from .forms import SearchForm, SignUpForm
from django.contrib.auth import authenticate, login as django_login, logout
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    setting = Setting.objects.get()
     # ... Outfit kategorisinin ID'sini veya adını bulun
    men_outfit_category = Category.objects.get(title="Men Outfit")
    women_outfit_category = Category.objects.get(title="Women Outfit")
    kid_outfit_category = Category.objects.get(title="Kid Outfit")

    
    # ... Outfit kategorisine ait ürünleri çekin
    slider_man = Product.objects.filter(category=men_outfit_category)[:4]
    slider_women = Product.objects.filter(category=women_outfit_category)[:4]
    slider_kid = Product.objects.filter(category=kid_outfit_category)[:4]
    current_user = request.user
    request.session['cart_items'] = ShopCard.objects.filter(user_id=current_user.id).count() #Show Count of Items in Cart
    
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
    comments = Comment.objects.filter(product_id=id,status='True')
    context = {"urunler":urunler,
               "resimler":resimler,
               "comments":comments,}
    return render(request, "home/urun_detay.html",context)
    
def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            setting = Setting.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            
            context = {'products':products,
                        'category':category,
                        'setting':setting,
                        }
            return render(request, 'home/product_search.html',context) 
    return HttpResponseRedirect('/')


def product_search_auto(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = [product.title for product in products]
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Hatası! Kullanıcı adı veya şifre yanlış.")
            return redirect ('login')
            # Return an 'invalid login' error message.
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

from django.contrib.auth import login as django_login

# Your other imports and views...

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)  # Use django_login instead of login
            current_user = request.user
            data= UserProfile()
            data.user_id =current_user.id
            data.image = "images/users/user.png"
            data.save(
            messages.success(request , "Sitemize Hoş Geldiniz")
            )
        else:
            form.errors
            return redirect("signup")
        
        return HttpResponseRedirect("/")
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'home/signup.html', context)



