from django.conf import settings
from django.contrib.auth import logout
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import FormMessagesMixin
from braces.views import LoginRequiredMixin

from .forms import  BeerCreateForm, BeerUpdateForm
from .models import Beer
from taps.models import Tap
from kegs.models import Keg


def home(request):
    """The main tap screen"""
    taps = Tap.objects.order_by('number')
    return render(request,'home.html',{'taps': taps, })

def dashboard(request):
    """The configuration dashboard"""
    kegstats = {}
    allkegs = Keg.objects.count()
    print allkegs
    for code, status in Keg.KEG_STATUS_CODES:
        kegcount = Keg.objects.filter(kegstatus = code).count()
        print "%s: %s" % (status, kegcount)
        kegstats[status] = kegcount

    print kegstats
    return render(request,'dashboard.html',
            {'allkegs': allkegs, 'kegstats': kegstats })

class BeerCreate(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a beer recipe
    """
    model = Beer
    success_url = reverse_lazy('beer:list')
    form_class = BeerCreateForm
    form_valid_message = _(u"Beer was created. All hail beer!")
    form_invalid_message = _(u"Something went wrong, beer was not saved")

    raise_exception = False
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        from django.utils.text import slugify
        form.instance.slug = slugify(form.instance.name)
        form.save()
        return super(BeerCreate, self).form_valid(form)


class BeerUpdate(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update an existing beer
    """
    model = Beer
    success_url = reverse_lazy('beer:list')
    form_class = BeerUpdateForm
    form_valid_message = _(u"Beer was updated. All hail beer!")
    form_invalid_message = _(u"Something went wrong, changes were not saved")

    raise_exception = False
    login_url = settings.LOGIN_URL


class BeerDelete(LoginRequiredMixin, DeleteView):
    """Delete a beer
    """
    model = Beer
    success_url = reverse_lazy('beer:list')

    raise_exception = False
    login_url = settings.LOGIN_URL


class BeerList(ListView):
    """List of beers"""
    model = Beer


def BeerDetail(request, slug):
    """Show the details of a beer"""
    beer = get_object_or_404(Beer, slug=slug)
    return render(request, 'beers/beer_detail.html', 
            {'beer': beer, })

def Beer_json(request):
    """Ajax callback for when a beer is selected, so that the
        estimated values for OG, FG, IBU, SRM can be filled in."""
    if request.method == 'POST':
         beer_id = request.POST.get('pk')
    if request.method == 'GET':
         beer_id = request.GET.get('pk')
    beer = get_object_or_404(Beer, pk=beer_id)
    data = serializers.serialize("json", [beer])
    print data
    return HttpResponse(data, content_type='application/json')

def logout_page(request):
    """
        Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')
