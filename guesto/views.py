from django.http import HttpResponse
from django.shortcuts import render,redirect
from menu.models import Category,Dish
from about_guesto.models import History
from team.models import Team
from booking.models import Booking
from events.models import Events
from contact_info.forms import UserMessageForm




def get_main_page(request):


    if request.method == "POST":
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")


    categories = Category.objects.filter(is_visible=True).order_by("category_order")
    history = History.objects.filter
    team = Team.objects.filter
    booking = Booking.objects.filter
    events = Events.objects.filter
    form = UserMessageForm()



    for item in categories:
        item.dishes = Dish.objects.filter(category=item.id)
    special_menu = Dish.objects.filter(category__title="Акції")


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
                "categories": categories,
               "special_menu": special_menu,
               "history":history,
               "team": team,
               "booking":booking,
               "events":events,
               "form":form

               }
    return render(request, 'index.html', context=context)


def dish_inform(request):
    return render(request,"information.html")