from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('api/auth/login/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('api/auth/register/', views.RegisterView.as_view(), name='register'),
]
