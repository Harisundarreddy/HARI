from django.shortcuts import render
from django.views.generic import View,ListView,DetailView
from TestApp.models import P

# Create your views here.
class Plistview(ListView):
    model=P

class Pdetailview(DetailView):
    model=P