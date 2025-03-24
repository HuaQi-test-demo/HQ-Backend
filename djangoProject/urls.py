"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from huaqi import views
from django.conf import settings
urlpatterns = [
    #    path("admin/", admin.site.urls),
    path('login1/', views.login),
    path('register1/',views.register),
    # path('table/',views.table),
    path('submit1/',views.submit_view),
    path('multi_currency1/',views.multi_currency),
    path('currency_pair1/',views.currency_pair),
    path('generate_pdf1/',views.generate_smart_pdf),

]
