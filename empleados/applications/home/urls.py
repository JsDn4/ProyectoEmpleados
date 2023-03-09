from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista_prueba/', views.ModeloPruebaListView.as_view())
]