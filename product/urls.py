from django.urls import path 
from . views import ProductDetail,Productliist ,Brandlist ,Brandetail,quaryset_debug
from .api import product_list_api,product_detail_api,productlistapi,productdetailapi,brandlistapi,branddetailapi



urlpatterns=[

path('',Productliist.as_view()),
path('debug',quaryset_debug),
path('<slug:slug>',ProductDetail.as_view()),
path('brands/',Brandlist.as_view()),
path('brands/<slug:slug>/',Brandetail.as_view()),

#api 
path('api/list',productlistapi.as_view()),
path('api/list/<int:pk>',productdetailapi.as_view()),
path('brands/api/list',brandlistapi.as_view()),
path('brands/api/list/<int:pk>',branddetailapi.as_view()),
]