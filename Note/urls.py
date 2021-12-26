from django.urls import path
from . import views as assets
urlpatterns = [
    path('', assets.index, name='index'),
    path('create/', assets.create, name='create'),
    path('update/<str:id>/', assets.view, name='view')
]
