from django.urls import path

from statistic import views

urlpatterns = [
    path('', views.StatisticList.as_view(), name='list'),
]
