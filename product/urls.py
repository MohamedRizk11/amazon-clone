from django.urls import path 

from . views import ProductDetail,Productliist



urlpatterns=[

path('',Productliist.as_view()),
path('<int:pk>',ProductDetail.as_view()),



]