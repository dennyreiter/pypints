from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from beers.models import Beer

# Create your views here.

def home(request):
     return render(request,'beers/home.html',{})

def config(request):
     return render(request,'beers/config.html',{})

class BeerCreate(CreateView):
    """Create a beer recipe
    """
    model = Beer
    success_url = reverse_lazy('beer_list')


class BeerUpdate(UpdateView):
    """Update an existing beer
    """
    model = Beer
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('beer_list')


class BeerDelete(DeleteView):
    """Delete a beer
    """
    model = Beer
    success_url = reverse_lazy('address_list')


class BeerList(ListView):
    """List of beers"""
    model = Beer


def BeerDetail(request, slug):
    """Show the details of a beer"""
    beer = get_object_or_404(Beer, slug=slug)
    print beer
    return render(request, 'beers/beer_detail.html', {'beer': beer,})

