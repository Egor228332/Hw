from django.http import HttpResponse
from django.shortcuts import render
from menu.models import Category,Dish




def get_main_page(request):

    category = Category.objects.all().order_by("category_order")
    dishes = Dish.objects.all().order_by("category_id")

    dish_1 = {
        'title': 'Яловичина від шефу',
        'description': 'Протягом цієї п\'ятирічки в ґрунт було висаджено гарбуз, шпинат та цілющий фенхель.'
    }
    dish_2 = {
        'title': 'Яловичина від шефу',
        'description': 'Протягом цієї п\'ятирічки в ґрунт було висаджено гарбуз, шпинат та цілющий фенхель.'
    }
    dish_3 = {
        'title': 'Яловичина від шефу',
        'description': 'Протягом цієї п\'ятирічки в ґрунт було висаджено гарбуз, шпинат та цілющий фенхель.'
    }
    context = {'title': 'Guesto Cafe',
               'about_title': 'Наша історія',
               'about_info': "Протягом цієї п\'ятирічки в ґрунт було висаджено гарбуз, шпинат та цілющий фенхель. Протягом цієї п'ятирічки в ґрунт було висаджено гарбуз, шпинат та цілющий фенхель. Протягом цієї п\'ятирічки в ґрунт було висаджено гарбуз, шпинат та цілющий фенхель.",
               'dishes': [dish_1, dish_2, dish_3],
               "categories": category,
               "dish": dishes
               }
    return render(request, 'index.html', context=context)

def event(request):
    return render(request,"event.html")
def dish_inform(request):
    return render(request,"information.html")