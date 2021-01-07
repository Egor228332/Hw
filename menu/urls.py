from django.urls import path
from .views import add_category,dish_detail,add_dish

urlpatterns = [
    path('add_category/', add_category,name="add category"),
    path("add_dish/",add_dish,name="add_dish"),
    path("<int:dish_id>/",dish_detail,name="dish_detail")

]
