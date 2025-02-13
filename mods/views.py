from django.shortcuts import render
from django.views.generic import ListView
from .models import ModList

class ModListView(ListView):
    template_name = 'mods/mods-list.html'
    model = ModList
    context_object_name = 'mods_list'