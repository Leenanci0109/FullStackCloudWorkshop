from django.urls import path
from loginpage import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
      path('', views.loginauth, name='loginauth')
]