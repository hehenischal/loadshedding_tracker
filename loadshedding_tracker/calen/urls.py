from django.urls import path
from . import views

urlpatterns = [
    path('ward/<int:ward_number>/', views.calendar_view, name='calendar_view'),
    path('', views.calendar_view, name='calendar_view'),
]

