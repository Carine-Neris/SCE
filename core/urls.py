from django.urls import path
from .views import index,contato,produto


urlpatterns = [
    path('',index,name='home'),
    path('contato/',contato, name='contato'),
    path('produto/',produto, name='produto')
] 