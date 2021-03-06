import random
import string

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def unique_slug_generator(instance):
    new_order_id = random_string_generator()

    klass = instance.__class__
    qs_exists = klass.objects.filter(order_id=new_order_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_order_id