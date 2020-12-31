"""rich_text_editor_using_cke_editor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('send/',views.send),
    path('contract/<int:id>/',views.GeneratePdf.as_view()),
    path('clientform/',views.clientForm),
    path('vendorform/',views.vendorForm),
    path('matchview/',views.match_view,name="matchview"),
    path('match/<int:cid>/<int:vid>/',views.match_client_vendor),
    path('match/<int:cid>/<int:vid>/numberofphases/',views.number_of_phases),
    path('getphases/<int:cid>/<int:vid>/',views.get_phases)
]
