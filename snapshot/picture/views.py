from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView
from .models import Collect
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'picture/index.html'

    def get_queryset(self):
     return Collect.objects.all()

class PictureCreate(CreateView):
    model = Collect
    fields = ['name', 'nick_name', 'about', 'image', 'caption', 'description']

class DetailView(generic.DetailView):
    model = Collect
    template_name = 'picture/detail.html'

