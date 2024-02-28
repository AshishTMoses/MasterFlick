from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from Backend.models import CatDb, MultiDb, MalDb
from Frontend.models import SubscribeDb
from django.core.mail import send_mail, EmailMessage
from MovieProject import settings
from django.contrib import messages
from django.core.validators import validate_email

import razorpay


# Create your views here.


def home_page(request):
    data = MultiDb.objects.all()
    item = MalDb.objects.all()
    return render(request, "Home.html",{'data': data, 'item':item})


def single_mult_page(request, videoid):
    video = MultiDb.objects.get(id=videoid)
    return render(request, "Singleview_mult.html", {'video': video})


def mal_film_single_page(request, malid):
    mal = MalDb.objects.get(id=malid)
    return render(request, "Mal_film_single_view.html", {'mal':mal})


def signup(request):
    return render(request,"Signup.html")

def save_signup(request):
    if request.method == "POST":
        mail = request.POST.get('email')
        unm = request.POST.get('username')
        pwd = request.POST.get('password')
        if SubscribeDb.objects.filter(username=unm):
            messages.error(request, "Username Already exist...Try some other username")
            return redirect(signup)
        if SubscribeDb.objects.filter(email=mail):
            messages.error(request, "Email id already exists please try different email")
            return redirect(signup)
        if len(unm)<4:
            messages.error(request,"Username must be greater than 4 character")
            return redirect(signup)
        # if mail is not validate_email:
        #     messages.error(request,"Email id doesnot exist")
        #     return redirect(signup)
        if not unm.isalnum():
            messages.error(request,"Username Must be alphanumeric")
            return redirect(signup)
        if SubscribeDb.objects.filter(password=pwd):
            messages.error(request,"Password already taken please try different one")

        obj = SubscribeDb(email=mail, username=unm, password=pwd)
        obj.save()
        messages.success(request, 'Account Created Successfully!')
        subject = "Welcome to masterflick"
        message = "Hello" + obj.username + "!!\n" "Welcome to MasterFlick!! \n Thankyou for connecting with us \n \n Thanking you \n Mater Flick admin"
        from_email = settings.EMAIL_HOST_USER
        to_list = [obj.email]
        send_mail(subject,message, from_email, to_list,fail_silently=True)
        return redirect(Subscription_page)




def Subscription_page(request):
    return render(request, "Subscription.html")

def payment(request):
    if request.method=="POST":
        amount=50000
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_IzIBFTmzd3zzKk','mMvIdZd7a4EU1pMd9tSQEbE0'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"payment.html")

def login_page(request):
    return render(request, "login.html")

def user_login(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if SubscribeDb.objects.filter(username=un, password=pwd).exists():
            request.session['username']=un
            request.session['password']=pwd
            messages.success(request, 'Logged Successfully!')
            return redirect(home_page)
        else:
            messages.error(request,'incorrect password or username')
            return redirect(login_page)
    return redirect(login_page)

def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, 'LoggedOut Successfully!')
    return redirect(home_page)

def cat_view_all(request):
    data = MultiDb.objects.all()
    return render(request, "Viewall_mult.html", {'data':data})

def mal_view_all(request):
    mal = MalDb.objects.all()
    return render(request, "Mal_viewall.html", {'mal':mal})

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        data = None  # Initialize data to None
        mal = None   # Initialize mal to None

        if query:
            data = MultiDb.objects.filter(Title__icontains=query)
        else:
            print("No results for MultiDb")

        if query:
            mal = MalDb.objects.filter(MalTitle__icontains=query)
        else:
            print("No results for MalDb")

        return render(request, "searchbar.html", {'data': data, 'mal': mal})











