from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.post_list, name="list"),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/edit/', views.edit, name='edit')
]
