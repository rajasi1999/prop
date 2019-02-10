from django.urls import path
from django.conf.urls import url,include
from . import views

app_name = 'portal'

urlpatterns = [
path('register/student', views.register,name='student_register'),
path('login/', views.user_login, name='user_login'),
path('register/college', views.register1, name='college_register'),
]
