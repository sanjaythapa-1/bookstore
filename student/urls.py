from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.RegistrationListAPIView.as_view(), name='registration-list'),
    
    # path('<int:pk>/', views.RegistrationDetailAPIView.as_view(), name='registration-detail'),
]