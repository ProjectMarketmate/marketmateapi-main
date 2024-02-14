from django.urls import path

from api.views import OrderItemlistApiview, ProductCategoryFilterAPIView, ProductdetailApiview, UserListApiview, UserdetailApiview, ProductListApiview 

urlpatterns=[
    path('users/',UserListApiview.as_view()),
    path('users/<int:pk>/',UserdetailApiview.as_view()),
    path('products/',ProductListApiview.as_view()) ,
    path('products/<int:pk>/',ProductdetailApiview.as_view()),
    path('products/category/<int:cat>/',ProductCategoryFilterAPIView.as_view()),
    path('orders/',OrderItemlistApiview.as_view())

]