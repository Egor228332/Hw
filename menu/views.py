from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish
from .forms import CategoryForm,DishForm


def dish_detail(request,dish_id):
    dish = Dish.objects.get(pk=dish_id)
    return HttpResponse(f"<h1>{dish.title}</h1><h1>{dish.price}</h1>")




def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponse("Add Suc")
    else:
        form = CategoryForm()
        return render(request, "add_category.html", context={"form":form})

def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse("add_suc")
    else:
        form = DishForm()
        return render(request,"add_dish.html",context={"form":form})



def list_categories(request):
    context = {}
    return render(request, 'index.html', context=context)