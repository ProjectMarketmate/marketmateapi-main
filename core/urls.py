from django.urls import path,include



urlpatterns=[
  path('app/',include('core.api.app.urls')),
  path('delivery/',include('core.api.delivery.urls'))
]