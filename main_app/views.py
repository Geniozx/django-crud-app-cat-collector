# main_app/views.py

from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView
from .models import Cat


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

    # main_app/views.py
def about(request):
    return render(request, 'about.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

# views.py

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    


