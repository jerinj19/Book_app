from django.contrib.auth import login
from django.urls import path
from adminapp import views

urlpatterns = [
    path('index/', views.index, name="index"),
    # category
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategory', views.savecategory, name="savecategory"),
    path('viewcategory/', views.viewcategory, name="viewcategory"),
    path('edit_category/<int:e_id>/', views.editcategory, name="editcategory"),
    path('update_category/<int:B_id>/', views.updatecategory, name="updatecategory"),
    path('delete_category/<int:cat_id>/',views.delete_category,name="delete_category"),
    path('admin_login_page/', views.admin_login_page, name="admin_login_page"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    # book
    path('add_book/',views.addbook,name="add_book"),
    path('savebook/',views.savebook,name="savebook"),
    path('displaybook/',views.displaybook,name="displaybook"),
    # login
    path('login1/', views.admin_login, name="admin_login"),

    # webapp
    path('viewcontact/',views.viewcontactmessage,name="viewcontact")


]
