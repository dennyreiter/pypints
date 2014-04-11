from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.views import generic
#from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from forms import TapListForm, BeerForm

from beers.models import Beer, Keg, Tap, SrmRgb
from braces.views import LoginRequiredMixin
from braces.views import FormMessagesMixin


def home(request):
    taps = Tap.objects.order_by('number')
    print taps
    return render(request,'beers/home.html',{'taps': taps, })

def dashboard(request):
    return render(request,'beers/dashboard.html',{})

class BeerCreate(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a beer recipe
    """
    model = Beer
    success_url = reverse_lazy('beer_list')
    form_class = BeerForm
    form_valid_message = _(u"Beer was created. All hail beer!")
    form_invalid_message = _(u"Something went wrong, beer was not saved")

    raise_exception = True

    def form_valid(self, form):
        from django.utils.text import slugify
        form.instance.slug = slugify(form.instance.name)
        form.save()
        return super(BeerCreate, self).form_valid(form)

class BeerUpdate(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update an existing beer
    """
    model = Beer
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('beer_list')
    form_valid_message = _(u"Beer was updated. All hail beer!")
    form_invalid_message = _(u"Something went wrong, changes were not saved")

    raise_exception = True


class BeerDelete(LoginRequiredMixin, DeleteView):
    """Delete a beer
    """
    model = Beer
    success_url = reverse_lazy('beer_list')

    raise_exception = True


class BeerList(ListView):
    """List of beers"""
    model = Beer


def BeerDetail(request, slug):
    """Show the details of a beer"""
    beer = get_object_or_404(Beer, slug=slug)
    return render(request, 'beers/beer_detail.html', 
            {'beer': beer, })

def Beer_json(request):
    if request.method == 'POST':
         beer_id = request.POST.get('pk')
    if request.method == 'GET':
         beer_id = request.GET.get('pk')
    beer = get_object_or_404(Beer, pk=beer_id)
    data = serializers.serialize("json", [beer])
    return HttpResponse(data, content_type='application/json')

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


class TapList(ListView):
    """List of Taps"""
    model = Tap


class TapUpdate(LoginRequiredMixin, UpdateView):
    """Update an existing keg
    """
    model = Tap
    form_class = TapListForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tap_list')

    raise_exception = True


class RssTapFeed(Feed):
    title = "PyPints Tap List"
    link = "/"
    description = "What's currently being poured."

    def items(self):
        return Tap.objects.filter(active=True)

    def item_title(self, item):
            return item.beer.name

    def item_description(self, item):
            return item.beer.notes

    def item_link(self, item):
            return self.link


class AtomTapFeed(RssTapFeed):
    feed_type = Atom1Feed
    subtitle = RssTapFeed.description
