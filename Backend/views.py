from django.shortcuts import render, redirect, reverse
from Backend.models import CatDb, MultiDb, MalDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def index_page(request):
    return render(request, "index.html")


def category_page(request):
    return render(request, "AddCategory.html")


def save_cat(request):
    if request.method == "POST":
        cname = request.POST.get('Name')
        lan = request.POST.get('language')
        gen = request.POST.get('genre')
        obj = CatDb(Cat_Name=cname, Language=lan, Genre=gen)
        obj.save()
        messages.success(request, "Category Added Successfully!!...")
        return redirect(category_page)


def cat_disp(request):
    details = CatDb.objects.all()
    return render(request, "CategoryDisplay.html", {'details': details})


def edit_cat(request, dataid):
    data = CatDb.objects.get(id=dataid)
    return render(request, "CategoryEdit.html", {'data': data})


def update_cat(request, dataid):
    if request.method == "POST":
        cname = request.POST.get('Name')
        lan = request.POST.get('language')
        gen = request.POST.get('genre')
        CatDb.objects.filter(id=dataid).update(Cat_Name=cname, Language=lan, Genre=gen)
        messages.success(request, "Category Updated Successfully!!...")
        return redirect(cat_disp)


def remv_cat(request, dataid):
    cn = CatDb.objects.filter(id=dataid)
    cn.delete()
    messages.error(request, "Category Deleted Successfully!!...")
    return redirect(cat_disp)


def multimedia_page(request):
    doc = CatDb.objects.all()
    return render(request, "AddMultimedia.html", {'doc': doc})


def save_multimedia(request):
    if request.method == "POST":
        mname = request.POST.get('tname')
        mlan = request.POST.get('lname')
        mgen = request.POST.get('gen')
        title = request.POST.get('title')
        desc = request.POST.get('description')
        about = request.POST.get('about')
        cast = request.POST.get('cast')
        mfile = request.FILES['file']
        img = request.FILES['image']
        obj = MultiDb(Multi_name=mname, Multi_lang=mlan, Multi_genre=mgen, Title=title, Description=desc, About=about, Cast=cast, File=mfile, image=img)
        obj.save()
        messages.success(request, "Multimedia Details Added Successfully!!...")
        return redirect(multimedia_page)


def mult_display(request):
    show = MultiDb.objects.all()
    return render(request, "MultimediaDisplay.html", {'show': show})


def edit_mult(request, dataid):
    data = CatDb.objects.all()
    info = MultiDb.objects.get(id=dataid)
    return render(request, "MultimediaEdit.html", {'data': data, 'info': info})


def update_mult(request, dataid):
    if request.method == "POST":
        mname = request.POST.get('tname')
        mlan = request.POST.get('lname')
        mgen = request.POST.get('gen')
        title = request.POST.get('title')
        desc = request.POST.get('description')
        about = request.POST.get('about')
        cast = request.POST.get('cast')

        try:
            vid = request.FILES['file']
            img = request.FILES['image']
            fs = FileSystemStorage()
            file1 = fs.save(vid.name, vid)
            file2 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            # Retrieve the MultiDb object once
            multimedia_obj = MultiDb.objects.get(id=dataid)
            file1 = multimedia_obj.File
            file2 = multimedia_obj.image

        # Use the retrieved values to update the database
        MultiDb.objects.filter(id=dataid).update(
            Multi_name=mname, Multi_lang=mlan, Multi_genre=mgen,
            Title=title, Description=desc, About=about, Cast=cast,
            image=file2, File=file1
        )

        messages.success(request, "Multimedia Details Updated Successfully!!...")
        return redirect(mult_display)


def mult_delt(request, dataid):
    cl = MultiDb.objects.filter(id=dataid)
    cl.delete()
    messages.error(request, "Multimedia Details Deleted Successfully!!...")
    return redirect(mult_display)


def admin_login_page(request):
    return render(request, "Admin_login.html")


def adminlogin(request):
    if request.method == "POST":
        usn = request.POST.get('user_name')
        psw = request.POST.get('pass_word')
        if User.objects.filter(username__contains=usn).exists():
            conf = authenticate(username=usn, password=psw)
            if conf is not None:
                login(request, conf)
                request.session['username'] = usn
                request.session['password'] = psw
                messages.success(request, "Admin Logged in Successfully!!...")
                return redirect(index_page)
            else:
                messages.error(request, "Please enter username and password to login")
                return redirect(admin_login_page)
        else:
            messages.error(request, "Admin Access STOPPED!!!!...Wrong Username or Password...")
            return redirect(admin_login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Admin Logged out Successfully!!...")
    return redirect(admin_login_page)


def add_mallu_film(request):
    return render(request, "Add_mal_film.html")

def save_mallu_film(request):
    if request.method == "POST":
        title = request.POST.get('title')
        malgen = request.POST.get('genre')
        maldesc = request.POST.get('desc')
        cast = request.POST.get('cast')
        dur = request.POST.get('duration')
        vid = request.FILES['video']
        img = request.FILES['image']
        obj = MalDb( MalTitle=title,genre=malgen,description=maldesc,cast=cast,time=dur,vid=vid,img=img)
        obj.save()
        messages.success(request, "Malayam Films Details Added Successfully!!...")
        return redirect(add_mallu_film)

def display_mal_film(request):
    now = MalDb.objects.all()
    return render(request, 'Display_mal_film.html',{'now': now})

def edit_mal_film(request, dataid):
    data = MalDb.objects.get(id=dataid)
    return render(request, 'Edit_mal_film.html', {'data': data})

def update_mal_film(request, dataid):
    if request.method == "POST":
        mtitle = request.POST.get('title')
        mgen = request.POST.get('genre')
        des = request.POST.get('desc')
        cast = request.POST.get('cast')
        dur = request.POST.get('duration')

        try:
            video = request.FILES['video']
            image = request.FILES['image']
            fs = FileSystemStorage()
            file1 = fs.save(video.name, video)
            file2 = fs.save(image.name, image)
        except MultiValueDictKeyError:
            # Retrieve the MultiDb object once
            mal_film_obj = MalDb.objects.get(id=dataid)
            file1 = mal_film_obj.vid
            file2 = mal_film_obj.img
        MalDb.objects.filter(id=dataid).update(
            MalTitle=mtitle,  genre=mgen, description=des,
            cast=cast, time=dur, img=file2, vid=file1
        )
        messages.success(request, "Malayam Films Details Edited Successfully!!...")
        return redirect(display_mal_film)

def cnc_mal_film(request, dataid):
    cnc = MalDb.objects.filter(id=dataid)
    cnc.delete()
    return redirect(display_mal_film)










