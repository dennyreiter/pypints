from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import FormMessagesMixin
from braces.views import LoginRequiredMixin

from .models import Keg


class KegList(ListView):
    """List of beers"""
    model = Keg


class KegDetail(DetailView):
    """Show the details of a keg"""
    model = Keg


class KegCreate(LoginRequiredMixin, CreateView):
    """Create a keg
    """
    model = Keg
    success_url = reverse_lazy('keg_list')

    raise_exception = True


class KegUpdate(LoginRequiredMixin, UpdateView):
    """Update an existing keg
    """
    model = Keg
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('keg_list')

    raise_exception = True


class KegDelete(LoginRequiredMixin, DeleteView):
    """Delete a keg
    """
    model = Keg
    success_url = reverse_lazy('keg_list')

    raise_exception = True

