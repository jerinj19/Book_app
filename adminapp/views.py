from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from adminapp.models import Book_category,Book
from webapp.models import Contactdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, "index.html")


def addcategory(request):
    return render(request, "add_category.html")


def savecategory(request):
    if request.method == "POST":
        name = request.POST.get('c_name')
        description = request.POST.get('c_desc')
        image = request.FILES['c_img']
        obj = Book_category(Category_name=name,
                            Category_description=description,
                            Category_image=image)
        obj.save()
        return redirect(addcategory)


def viewcategory(request):
    category = Book_category.objects.all()
    return render(request, "view_category.html", {'category': category})


def editcategory(request, e_id):
    edit = Book_category.objects.get(id=e_id)
    return render(request, "edit_category.html", {'edit': edit})


def updatecategory(request, B_id):
    if request.method == "POST":
        name = request.POST.get('c_name')
        description = request.POST.get('c_desc')
        try:
            img = request.FILES['c_img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Book_category.objects.get(id=B_id).Category_image

        Book_category.objects.filter(id=B_id).update(
            Category_name=name,
            Category_description=description,
            Category_image=file
        )
        return redirect(viewcategory)

def delete_category(request,cat_id):
    data=Book_category.objects.filter(id=cat_id)
    data.delete()
    return redirect(viewcategory)


def addbook(request):
    categorys=Book_category.objects.all()
    return render(request, "add_book.html",{'categorys':categorys})





def savebook(request):
    if request.method == "POST":
        tittle = request.POST.get('b_title')
        author=request.POST.get('b_author')
        category=request.POST.get('b_category')
        price=request.POST.get('b_price')
        publisher=request.POST.get('b_pub')
        description=request.POST.get('b_desc')
        book_image=request.FILES['b_img']
        obj=Book(Book_image=book_image,
                 Book_Description=description,
                 Book_Publisher=publisher,
                 Book_Price=price,
                 Category=category,
                 Book_author=author,
                 Book_Tittle=tittle)
        obj.save()
        return redirect(addbook)
def displaybook(request):
    book_data=Book.objects.all()
    return render(request,"view_book.html",{'book_data':book_data})





def admin_login_page(request):
    return render(request, "admin_login.html")


def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data = authenticate(username=un, password=pw)

            if data is not None:
                login(request, data)
                request.session['username'] = un
                request.session['password'] = pw
                return redirect(index)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def viewcontactmessage(request):
    data=Contactdb.objects.all()
    return render(request,"viewcontact.html",{'data':data})
