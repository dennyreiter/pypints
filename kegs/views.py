from django.conf import settings
from django.core.urlresolvers import reverse_lazy
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import FormMessagesMixin
from braces.views import LoginRequiredMixin

from .forms import KegCreateForm, KegUpdateForm
from .models import Keg


class KegList(ListView):
    """List of beers"""
    model = Keg


class KegDetail(DetailView):
    """Show the details of a keg"""
    model = Keg


class KegCreate(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a keg
    """
    model = Keg
    form_class = KegCreateForm
    success_url = reverse_lazy('keg:list')
    form_valid_message = _(u"New keg was created.")
    form_invalid_message = _(u"Something went wrong, keg was not created.")

    raise_exception = False
    login_url = settings.LOGIN_URL


class KegUpdate(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update an existing keg
    """
    model = Keg
    form_class = KegUpdateForm
    success_url = reverse_lazy('keg:list')
    form_valid_message = _(u"Keg was updated.")
    form_invalid_message = _(u"Something went wrong, keg was not updated.")

    raise_exception = False
    login_url = settings.LOGIN_URL


class KegClean(LoginRequiredMixin,View):
    """Change a keg to be clean
    """

    raise_exception = False
    login_url = settings.LOGIN_URL

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('CleanKeg'):
            kegid = int(self.request.POST.get('id'))
            keg = Keg.objects.get(pk = kegid)
            print "Cleaning keg %d" % kegid
            keg.kegstatus = 'CLEAN'
            keg.save()

        return HttpResponseRedirect(reverse_lazy('keg:list'))


class KegDelete(LoginRequiredMixin, DeleteView):
    """Delete a keg
    """
    model = Keg
    success_url = reverse_lazy('keg:list')

    raise_exception = False
    login_url = settings.LOGIN_URL


