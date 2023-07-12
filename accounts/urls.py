from django.urls import path

from accounts import views

urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='token_obtain_pair'),
]
