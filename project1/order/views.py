from django.contrib import messages
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from order.models import ShopCard,ShopCardForm,OrderForm,Order,OrderProduct
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

from product.models import Product
from home.models import UserProfile
# Create your views here.

def order(request):
    return HttpResponse("Order Page")

@login_required(login_url='/login') #Check Login
def addtocard(request,id):  #Sepete Ekleme Fonksiyonu
    url = request.META.get('HTTP_REFERER') # get last url
    checkproduct=ShopCard.objects.filter(product_id=id) #check product in shopcart
    if checkproduct: #update quantity if product is already exists
        control = 1
    else :
        control = 0
         
        
    if request.method == 'POST':
        form = ShopCardForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCard.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCard() #create relation with model
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save() #save data to table
            
                messages.success(request,"Ürün Başarı ile Sepete Eklenmiştir.")
        request.session['cart_items'] = ShopCard.objects.filter(user_id=current_user.id).count() #Show Count of Items in Cart
        return HttpResponseRedirect(url)
    
            
    else :
        current_user = request.user
        if control == 1:
            data = ShopCard.objects.get(product_id=id)
            data.quantity += 1
            data.save()
            messages.success(request,"Ürün Başarı ile Sepete Eklenmiştir.Teşekkür Ederiz.")
        else:
            current_user = request.user #Access User Session Information
            data = ShopCard() #create relation with model
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save() #save data to table
            messages.success(request,"Ürün Başarı ile Sepete Eklenmiştir.Teşekkür Ederiz.")
            return HttpResponseRedirect(url)
    request.session['cart_items'] = ShopCard.objects.filter(user_id=current_user.id).count() #Show Count of Items in Cart            
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shopcart(request): # Sepet Fonksiyonu
    current_user = request.user
    shopcart = ShopCard.objects.filter(user_id=current_user.id)  # Doğru sorgu yapısı burada kullanılıyor
    request.session['cart_items'] = ShopCard.objects.filter(user_id=current_user.id).count() #Show Count of Items in Cart

    for rs in shopcart:
        rs.total_price = rs.product.price * rs.quantity  # Calculate total price for each item

    total = sum(rs.total_price for rs in shopcart)  # Calculate the overall total
    context = {'shopcart': shopcart, 'total': total}
    return render(request, 'home/shopcard_product.html', context)

@login_required(login_url='/login')
def deleteformcart(request,id): # Sepetten silme fonksiyonu
    ShopCard.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCard.objects.filter(user_id=current_user.id).count() #Show Count of Items in Cart
    messages.success(request,"Ürün Başarı ile Sepetten Silinmiştir.")
    return redirect("shopcart")



# ********* ALIŞVERİŞİ TAMAMLA *********
@login_required(login_url='/login') #Check Login
def orderproduct(request): # Sİpariş tamamlama fonksiyonu
    current_user = request.user
    shopcart = ShopCard.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order() #create relation with model
            data.username = form.cleaned_data['username']
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            data.user_id = current_user.id
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save() #save data to table
            
            shopcart = ShopCard.objects.filter(user_id=current_user.id)
            for rs in shopcart:
                detial = OrderProduct()
                detial.order_id = data.id #Order Id
                detial.product_id = rs.product_id
                detial.user_id = current_user.id
                detial.quantity = rs.quantity
                detial.price = rs.product.price
                detial.amount = rs.amount
                detial.save()
                
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()
                
            ShopCard.objects.filter(user_id=current_user.id).delete() #Clear & Delete shopcart
            request.session['cart_items'] = 0
            messages.success(request,"Siparişiniz Başarı ile Tamamlanmıştır. Teşekkür Ederiz.")
            return render(request, 'home/shopcard_product.html',{"ordercode":ordercode})
        else :
            messages.warning(request,form.errors)
            return HttpResponseRedirect("/order/orderproduct")
        
        
    
    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {"shopcart":shopcart,
                "total":total,
                "form":form,
                "profile":profile,
                }
    return render(request, "order/order_form.html",context)