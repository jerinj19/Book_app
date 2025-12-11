from django.shortcuts import render, redirect
from adminapp.models import Book_category, Book
from webapp.models import RegisterDb,Contactdb,Cart
from django.contrib import messages

def homepage(request):
    category = Book_category.objects.all()
    book = Book.objects.all()
    return render(request, "homepage.html", {'category': category, 'book': book})


def contactpage(request):
    contact= Book_category.objects.all()
    return render(request, 'contact.html',{'contact':contact})


def aboutpage(request):
    data=Book_category.objects.all()
    return render(request, 'about.html',{'data':data})


def popularbooks(request):
    popular = Book_category.objects.all()
    return render(request, "popular_books.html", {'popular': popular})


def filtred_books(request, b_id):
    cat = Book_category.objects.all
    filters = Book.objects.filter(Category=b_id)
    bookcategory = Book.objects.filter(Category=b_id)
    return render(request, "filtered_books.html", {'filters': filters,
                                                   'cat': cat,
                                                   'bookcategory': bookcategory})


def single_book(request, book_id):
    single = Book.objects.get(id=book_id)
    return render(request, "single_book.html", {'single': single})


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "signin.html")


def saveuser(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        email = request.POST.get('u_email')
        passworrd = request.POST.get('U_pwd')
        confirm_password = request.POST.get('C_pwd')
        obj = RegisterDb(Name=name,
                         Email=email,
                         Password=passworrd,
                         Confirm_password=confirm_password)
        if RegisterDb.objects.filter(Name=name).exists():
            messages.warning(request,"User Already exists")
            return redirect(signup)
        elif RegisterDb.objects.filter(Email=email, ).exists():
            return redirect(signup)
        else:
            obj.save()
            return redirect(login)


def userlogin(request):
    if request.method == "POST":
        useremail = request.POST.get('E_mail')
        password = request.POST.get('Pass_w')
        if RegisterDb.objects.filter(Email=useremail, Password=password).exists():
            request.session['Email'] = useremail
            request.session['Password'] = password
            return redirect(homepage)
        else:
            return redirect(login)
    else:
        return redirect(login)


def userlogout(request):
    del request.session['Email']
    del request.session['Password']
    return redirect(homepage)

def saveContact(request):
    if request.method=="POST":
        name=request.POST.get('C_name')
        email = request.POST.get('C_email')
        mob = request.POST.get('C_mob')
        city = request.POST.get('C_city')
        type = request.POST.get('C_type')
        message = request.POST.get('C_message')
        obj=Contactdb(Contact_message=message,
                      Contact_name=name,
                      Contact_email=email,
                      Contact_phone=mob,
                      Contact_city=city,
                      Enquiry_type=type)
        obj.save()
    return redirect(contactpage)
def savecart(request):
    if request.method=="POST":
        email=request.POST.get('username')
        quantity=int(request.POST.get('quantity'))
        b_price=int(request.POST.get('price'))
        t_price=int(request.POST.get('total_price'))
        b_tittle=request.POST.get('book_name')
        book=Book.objects.filter(Book_Tittle=b_tittle).first()
        img=book.Book_image if book else None
        obj=Cart(username=email,Book_name=b_tittle,qty=quantity,price=b_price,total_price=t_price,Book_image=img)
        obj.save()
        return redirect(homepage)
def viewcart(request):
    item=Cart.objects.all()
    return render(request,"cart.html",{'item':item})