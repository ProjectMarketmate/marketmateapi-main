from django.urls import path
from account import views
from account.views import CustomUserAccountActivationView, CustomUserProfileView,CustomUserRegistrationView,CustomUserLoginView

urlpatterns = [
    path('register/', CustomUserRegistrationView.as_view(), name='register-user'),
     path('activate/', CustomUserAccountActivationView.as_view(), name='user-activate'),
     path('login/', CustomUserLoginView.as_view(), name='user-login'),
     path('profile/', CustomUserProfileView.as_view(), name='user-profile'),
    path('account/delete/', views.AccountDeleteAPIView.as_view(), name='account-delete'),
     
]
