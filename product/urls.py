from django.urls import path 

from . views import ProductDetail,Productliist ,Brandlist ,Brandetail



urlpatterns=[

path('',Productliist.as_view()),
path('<slug:slug>',ProductDetail.as_view()),

path('brands/',Brandlist.as_view()),
path('brands/<slug:slug>/',Brandetail.as_view()),

]