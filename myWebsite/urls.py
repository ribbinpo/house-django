from django.contrib import admin
from django.urls import path
from myWebsite import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path
from myWebsite import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index,name="index"),
    path("product/",views.product),
    path("addProduct/",views.addProduct),
    path("manageProduct/",views.manageProduct),
    path("manageAccount/",views.manageAccount),
    path("login/",views.login,name="login"),
    path("register/",views.register),
    path("loginMethod/",views.loginMethod,name="loginMethod"),
    path("recordHouse/",views.recordHouse,name="recordHouse"),
    path("deleteHouse/",views.deleteHouse,name="deleteHouse"),
    path("editHouse/",views.editHouse,name="editHouse"),
    path("logoutMethod/",views.logoutMethod,name="logoutMethod"),
    path("registMethod/",views.registMethod,name="registMethod"),
    path("loginWarning/",views.loginWarning,name="loginWarning"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)