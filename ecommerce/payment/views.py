from django.shortcuts import render
from .models import ShippingAddress

# Create your views here.

def checkout(request):

    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context = {"shipping": shipping_address}
            print("into try")

            return render(request, "payment/checkout.html", context=context)
        except:
            print("except try")
            return render(request, "payment/checkout.html")
    else:
        return render(request, "payment/checkout.html")
    
def complete_order(request):

    pass

def payment_success(request):

    return render(request, "payment/payment_success.html")


def payment_failed(request):

    return render(request, "payment/payment_failed.html")