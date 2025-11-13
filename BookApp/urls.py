
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from . import  settings
import adminapp.urls
import webapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminapp/',include(adminapp.urls)),
    path('webapp/',include(webapp.urls))
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
