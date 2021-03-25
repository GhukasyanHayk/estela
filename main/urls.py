from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'), 
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact_us/', views.contact_us, name='contact_us')
]
