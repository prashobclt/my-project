from django.urls import path
from . import views
app_name='doctor'
urlpatterns = [      
    path('login', views.loginfun, name='log_in')
]