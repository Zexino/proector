from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Categories(models.Model):
    category_name = models.CharField(max_length = 51, null = False)
    category_summury = models.CharField(max_length = 31, null = False)
    url_slug = models.CharField(max_length = 31, null = False, default="all")
    def __str__(self):
        return "Category : %s" %(self.category_name)



class Product(models.Model):
    tittle = models.CharField(max_length = 150)
    text = models.TextField()
    date = models.DateTimeField(auto_now = True)
    publishe_date = models.DateTimeField("date published")
    price = models.DecimalField(max_digits = 9,decimal_places=2)
    url_slug = models.CharField(max_length = 31, null = False, default = "default")
    news_category = models.ManyToManyField(Categories)
        
    image = models.ImageField(upload_to = 'img/', blank = True, null = True)
    def __str__(self):
        return "Post tittle: %s" %(self.tittle)

class CartItem(models.Model):
    cart_id = models.CharField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)
    quantity = models.IntegerField(default = 1)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, unique = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, unique = False, default=1)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']
    def total(self):
        return self.product.price
    def name(self):
        return self.product.tittle
    def price(self):
        return self.product.price 
    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    liked = models.ForeignKey(Product, on_delete = models.CASCADE)


class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    disliked = models.ForeignKey(Product, on_delete = models.CASCADE)
