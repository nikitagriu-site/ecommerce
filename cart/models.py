from django.db import models

from django.conf import settings

from products.models import Product

from django.db.models.signals import pre_save, post_save

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        if cart_id is None:
            print('Cart ID exists')
            cart_obj = cart_create()    
            request.session['cart_id'] = cart_obj.id
        else:
            qs = self.get_queryset().filter(id=cart_id)
            if qs.count() == 1:
                new_obj = False
                cart_obj = qs.first()
                if request.user.is_authenticated and cart_obj.user is None:
                    cart_obj.user = request.user
                    cart_obj.save()
                else:
                    cart_obj = Cart.objects.new(user=request.user)
                    new_obj = True
                    request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        print(user)
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)



class Cart(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)
    
def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    products = instance.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    instance.total = total 

pre_save.connect(pre_save_cart_receiver, sender=Cart)