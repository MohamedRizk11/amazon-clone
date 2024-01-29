from django.urls import path 

from . views import ProductDetail,Productliist ,Brandlist



urlpatterns=[

path('',Productliist.as_view()),
path('<slug:slug>',ProductDetail.as_view()),

path('brands/',Brandlist.as_view()),

]