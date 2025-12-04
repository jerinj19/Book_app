from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # <- empty string '' matches '/'
    path('contactpage/', views.contactpage, name='contact'),
    path('about/', views.about, name='about'),
    path('popular/', views.popular, name='popular'),
    path('filter/<b_id>/', views.filter, name='filter'),
    path('single/<int:book_id>/', views.single_book, name='single_book'),
    path('signup/', views.signup, name='signup'),
    path('savesignup/', views.save, name='save'),
    path('login/', views.login, name='userlogin'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='logout'),
    path('savecontact/', views.savecontact, name='contact'),
]
