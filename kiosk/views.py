from django.views.generic import ListView
from .models import Category, Item

class MenuListView(ListView):
    model = Category
    template_name = 'kiosk/menu_list.html'