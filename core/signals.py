from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save

from account.utils import Util
from core.models import Order



@receiver(post_save,sender = Order)
def update_order(sender, instance:Order, **kwargs):
    status = instance.status
    if status == Order.ORDER_STATUS.PENDING:
        status = "Placed"
    data ={
        "subject":f"Order {status}",
        "body":f"Your order {status},",
        "to_email":instance.user.email
    }
    Util.send_email(data)
        
        