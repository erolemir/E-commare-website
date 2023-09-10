from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput , Textarea
from product.models import Product

# Create your models here.

class Setting(models.Model):
    STATUS= (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    adress = models.CharField(blank = True ,max_length=150)
    phone = models.CharField(blank = True ,max_length=15)
    fax = models.CharField(blank = True ,max_length=150)
    email = models.CharField(blank = True ,max_length=50)
    smtpserver = models.CharField(blank = True ,max_length=20)
    smtpemail = models.CharField(blank = True ,max_length=50)
    smtppassword = models.CharField(blank = True ,max_length=10)
    smtpport = models.CharField(blank = True , max_length=5)
    icon = models.ImageField(upload_to='images/', blank = True)
    facebook = models.CharField(blank = True ,max_length=50)
    instagram = models.CharField(blank = True ,max_length=50)
    twitter = models.CharField(blank = True ,max_length=50)
    aboutus = RichTextUploadingField(blank = True )
    contact = RichTextUploadingField(blank = True )
    referances = RichTextUploadingField(blank = True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class ContactFormMessage(models.Model):
    STATUS= (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS,default="New") 
    ip = models.CharField(blank = True ,max_length=15)
    note = models.CharField(blank = True ,max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ["name","email","subject","message"]
        wigdets = {
            "name": TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            "subject": TextInput(attrs={'class':'input','placeholder':'Subject'}),
            "email": TextInput(attrs={'class':'input','placeholder':'Email Address'}),
            "message": Textarea(attrs={'class':'input','placeholder':'Your Message','rows':'5'}),
        }
    
