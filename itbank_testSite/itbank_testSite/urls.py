"""itbank_testSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from clientes import views as clientViews
from login import views as loginViews
from prestamos import views as prestamosViews
from cuentas import views as cuentaViews
from tarjetas import views as tarjetaViews
from sucursal import views as sucursalViews

urlpatterns = [
    path('', clientViews.home, name="home"),
    path('login/', loginViews.LoginPage, name="login"),
    path('logout/', loginViews.LogoutPage, name="logout"),
    path('prestamos/', prestamosViews.Prestamos, name="prestamos"),
    path('admin/', admin.site.urls),
    path('api/clientes/<int:pk>', clientViews.ClienteDetails.as_view()),
    path('api/cuentas/<int:pk>', cuentaViews.CuentaDetails.as_view()),
    path('api/prestamos/<int:pk>', prestamosViews.PrestamoDetails.as_view()),
    path('api/prestamos/', prestamosViews.PrestamoList.as_view()),
    path('api/sucursal/<int:pk>', prestamosViews.SucursalPrestamoList.as_view()),
    path('api/tarjetas/<int:pk>', tarjetaViews.ClientTarjetaList.as_view()),
    path('api/sucursales/', sucursalViews.SucursalList.as_view()),
]
