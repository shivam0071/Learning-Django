from . import views
from django.urls import path


app_name = 'isocal'

urlpatterns = [
    # post views
    path('', views.iso_cal_home, name='homepage'),
]
