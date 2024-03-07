from django.shortcuts import render
from. models import Category 

def get_category(request):
    categories = Category.objects.all()
    return render(request, {'categories': categories})