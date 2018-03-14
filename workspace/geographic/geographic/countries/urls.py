"""geographic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

#importo include de django.urls
from django.urls import path, include
#Importamos home
from countries.views import (
    CountryDetailView,
    CountryDetailIdView
    )

urlpatterns = [
    #En las urls de la app principal le diremos que procese nuestra vista de la mini-app
    # Si utilizo name puede hacer referencia de los templates
    #Valido que es un entero
    path('<int:id>/', CountryDetailIdView.as_view(), name="country_id_detail"),
    path('<code>/', CountryDetailView.as_view(), name="country_detail"),
]
