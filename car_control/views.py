from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import car
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'car_control/index.html'
    context_object_name = 'latest_car_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return car.objects.order_by('-mat')[:5]

class DetailView(generic.DetailView):
    model = car
    template_name = 'car_control/detail.html'