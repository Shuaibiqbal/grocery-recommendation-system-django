from django.urls import path 
from . import views
urlpatterns = [
    path('train/', views.train_view, name = "train_model"),
    path('recommend/', views.recommend_view, name='recommend'),
]