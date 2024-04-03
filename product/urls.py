from django.urls import path 
from . views import ProductDetail,Productliist ,Brandlist ,Brandetail,quaryset_debug
from .api import product_list_api,product_detail_api



urlpatterns=[

path('',Productliist.as_view()),
path('debug',quaryset_debug),
path('<slug:slug>',ProductDetail.as_view()),
path('brands/',Brandlist.as_view()),
path('brands/<slug:slug>/',Brandetail.as_view()),

#api 
path('api/list',product_list_api),
path('api/list/<int:product_id>',product_detail_api),

]