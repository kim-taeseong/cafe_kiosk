from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Category, Item

class MenuListView(ListView):
    model = Category
    template_name = 'kiosk/menu_list.html'

class MenuDetailView(DetailView):
    model = Item
    template_name = 'kiosk/menu_detail.html'

class MenuDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('kiosk:index')