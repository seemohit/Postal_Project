from django.urls import path
from . import  views
urlpatterns = [
    path('', views.mainpage),
    path('ins/', views.insertdata),
    path('insert', views.insertdata),
    path('postsubmit/', views.mainpage),
    path('show/', views.show),
    path('apply', views.mydata),
]
