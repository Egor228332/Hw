from django import forms
from .models import Category,Dish
from uuid import uuid4
from os import path
class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={"placeholder":"Назва категорії","required":"required"}))
    category_order = forms.IntegerField(widget=forms.TextInput(attrs={"Порядок категорії в меню":"Електрона пошта","required":"required"}))
    is_visible = forms.BooleanField(widget=forms.CheckboxInput(attrs={"required":"required"}))
    class Meta(object):
        model = Category
        fields = ("title","category_order","is_visible")
class DishForm(forms.ModelForm):
    def get_file_name_dishes(self,filename):
        ext = filename.split(".")[-1]
        filename = f"{uuid4()}.{ext}"
        return path.join("images/dishes", filename)
    title = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=7, decimal_places=2)
    description = forms.CharField(max_length=300)
    spicy = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects)
    photo = forms.ImageField()
    class Meta(object):
        model = Dish
        fields = ("title","price","description","spicy","category","photo")