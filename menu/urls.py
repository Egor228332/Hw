from django.urls import path
from .views import menu_categories, list_categories

urlpatterns = [
    path('', list_categories)
]
