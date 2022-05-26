from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('user_data', views.user_data, name='user_data'),
    path('user_data_applying', views.user_data_applying, name='user_data_applying'),
    path('registration', views.registration, name='registration'),
    path('discription', views.discription, name='discription'),
    path('purchase_confirmation', views.purchase_confirmation, name='purchase_confirmation'),
]
