from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput , Textarea
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    STATUS= (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)    
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '-'.join(full_path[::-1])
    
class Product(models.Model):
    STATUS= (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE) # Category tablosuyla ilişki kurulması
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    slug = models.SlugField(default="Kıyafet")
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    STATUS= (
        ('New', 'Yeni'),
        ('True', 'Göster'),
        ('False', 'Gösterme'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)# Product tablosuyla ilişki kurulması
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=150,blank=True)
    comment = models.TextField(max_length=255)
    rate = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return self.subject
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields =['subject','comment','rate']


    

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    images = models.ImageField(blank=True, upload_to='images/')
    
    
    def __str__(self):
        return self.title