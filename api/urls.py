from django.urls import path
from . import views as assets
urlpatterns = [
    path('', assets.notes, name='notes'),
    path('create/', assets.create, name='create'),
    path('note/<str:id>/', assets.note, name='note'),
    path('update/<str:id>/', assets.update, name='update'),
    path('delete/<str:id>/', assets.remove, name='remove'),
]
