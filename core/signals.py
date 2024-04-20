from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save

from account.utils import Util
from core.models import Order



@receiver(post_save,sender = Order)
def update_order(sender, instance:Order, **kwargs):
    data ={
        "subject":f"Order {instance.status}",
        "body":f"Your order {instance.status},",
        "to_email":instance.user.email
    }
    Util.send_email(data)
        
        