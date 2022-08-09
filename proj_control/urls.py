from xml.etree.ElementInclude import include
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('accounts/', include('app_accounts.urls'),name="accounts"),
    path('orden/',include('app_orden.urls'),name="orden"),
]
