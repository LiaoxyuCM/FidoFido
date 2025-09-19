"""
URL configuration for fidofido project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from django.urls import path, register_converter
from . import views  # Import your views module

class ColorModeConverter:
    regex = 'light|dark'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
    
register_converter(ColorModeConverter, 'colormode')

urlpatterns = [
    path('', views.index, name='index'),  # Redirect root URL to index view
    path('search/', RedirectView.as_view(url='/', permanent=True)),
    path('search/<str:query>/', views.search_passages, name='search_passages'),
    path('passage/', RedirectView.as_view(url='/', permanent=True)),
    path('passage/detail/<int:passage_id>/', views.detail, name='detail'),
    path('change_color_mode/<colormode:color_mode>/', views.change_color_mode, name='change_color_mode'),
]
