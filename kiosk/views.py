from django.views.generic import ListView, DetailView
from .models import Category, Item

class MenuListView(ListView):
    model = Category
    template_name = 'kiosk/menu_list.html'

class MenuDetailView(DetailView):
    model = Item
    template_name = 'kiosk/menu_detail.html'