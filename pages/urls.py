from django.urls import path
from . import views


app_name = 'pages'

urlpatterns = [

    path('help/', views.HelpPageView.as_view(), name='help'),
    path('services/', views.ServicePageView.as_view(), name='services'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('about/', views.AboutPageView.as_view(), name='about'), 
    path('', views.HomePageView.as_view(), name='home'),
    
]