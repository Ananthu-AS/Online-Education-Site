from django.http import HttpResponseBadRequest
from django.shortcuts import render,redirect
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from flask import Flask,request

from userapp.models import price
from django.contrib.auth.decorators import login_required
# Create your views here.
# def Home(request):
#     return render(request,"app.html")

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("rzp_test_acgCaQhDp1w1uK", "8egrozmgdp1GGzZ2DYvNNRcl"))

def app_create(request,id):
    if request.user.is_authenticated:
        data = price.objects.get(course=id)
        amount=data.price*100    
        return render(request,"app.html",{'data':data,'amount':amount})
    else:
        messages.error(request, "Login to continue.")
        return redirect("/")

@csrf_exempt
def app_charge(request,id):
    if request.method == 'POST':
        current=request.user
        data = price.objects.get(id=id)
        amount=data.price*100
        payment_id = request.POST.get('razorpay_payment_id')
        razorpay_client.payment.capture(payment_id, amount)
        return render(request,"charge.html",{'payment_id':payment_id,'data':data,'current':current})
    else:
        return HttpResponseBadRequest("payment unsuccessfull")

if __name__ == '__main__':
    app.run()
