from django.urls import include, path

from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing')
]
