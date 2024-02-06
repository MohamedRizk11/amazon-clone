from django.urls import path 

from . views import ProductDetail,Productliist ,Brandlist ,Brandetail,quaryset_debug



urlpatterns=[

path('',Productliist.as_view()),
path('debug',quaryset_debug),

path('<slug:slug>',ProductDetail.as_view()),

path('brands/',Brandlist.as_view()),
path('brands/<slug:slug>/',Brandetail.as_view()),

]