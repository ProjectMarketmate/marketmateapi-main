from django.urls import include, path


from core.api.app.banner import  OfferBannerListCreateAPIView
from core.api.app.order import OrderApiView, OrderCreateApiView,  OrderRetrieveUpdateDestroyAPIView,  StaffOrdersListApiView

from core.api.app.product import CategoryListAPIView, ProductListAPIView
from core.api.app.cart import CartItemDeleteApiView, CartItemListApiView, CartItemUpdateApiView
# from core.api.app.rating import RatingCreateAPIView
from core.api.app.toporders import  get_recommendations


urlpatterns=[
  path('products/',ProductListAPIView.as_view(),name="app-products"),
  path('cart/',CartItemListApiView.as_view()),
  path('cart/update/<int:pk>/',CartItemUpdateApiView.as_view()),
  path('cart/delete/<int:pk>/',CartItemDeleteApiView.as_view()),
  path('categories/',CategoryListAPIView.as_view()),
  path('order/',OrderApiView.as_view(),name="app-order"),
  path('order/create/',OrderCreateApiView.as_view(),name="app-order-create"),
  path('order/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
  path('offers/banners/', OfferBannerListCreateAPIView.as_view(), name='offer-banners'),
  path('staff/orders/', StaffOrdersListApiView.as_view(), name='staff-orders'),
  path('staff/orders/<int:pk>/',OrderRetrieveUpdateDestroyAPIView.as_view(), name='staff-order-detail'),
  path('toporders/', get_recommendations, name='get_recommendations'),
  # path('ratings/', RatingCreateAPIView.as_view(), name='rating-create'),
  path('recommendations/', get_recommendations, name='get_recommendations'),
  

]