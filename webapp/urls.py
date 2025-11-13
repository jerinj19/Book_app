from django.urls import path
from webapp import views
urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('contactpage/',views.contactpage,name="contact"),
    path('about/',views.aboutpage,name="about"),
    path('popular/',views.popularbooks,name="popular"),
    path('filter/<b_id>/',views.filtred_books,name="filter"),
    path('single/<int:book_id>/',views.single_book,name="single_book"),
    path('signup/',views.signup,name="signup"),
    path('savesignup/',views.saveuser,name="save"),
    path('login/',views.login,name="login"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="logout"),
    path('savecontact/',views.saveContact,name="contact")


]