
from django.urls import path
from WMS import views

urlpatterns = [
    path('', views.home, name='index'),
    path('Request/', views.wasterequest, name='request'),
    path('signup/', views.signup, name='signup'),
    path('services/',views.services, name='services'),
    path('signin/', views.signin, name='signin'),
    path('delete/<str:pk>/',views.delete, name='delete'),
    path('update/<str:pk>/', views.update, name='update')




]
