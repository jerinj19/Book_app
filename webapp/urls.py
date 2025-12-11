from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # <- empty string '' matches '/'
    path('contactpage/', views.contactpage, name='contact'),
    path('about/', views.aboutpage, name='about'),
    path('popular/', views.popularbooks, name='popular'),
    path('filter/<b_id>/', views.filtred_books, name='filter'),
    path('single/<int:book_id>/', views.single_book, name='single_book'),
    path('signup/', views.signup, name='signup'),
    path('savesignup/', views.saveuser, name='save'),
    path('login/', views.login, name='userlogin'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='logout'),
    path('savecontact/', views.saveContact, name='contact'),
    path('savecart',views.savecart,name="save_cart"),
    path('viewcart/',views.viewcart,name="view")
]
