from django.contrib.syndication.views import Feed
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import FormMessagesMixin
from braces.views import LoginRequiredMixin

from .forms import  BeerForm, BeerUpdateForm
from taps.forms import TapListForm
from .models import Beer
from taps.models import Tap
from kegs.models import Keg


def home(request):
    taps = Tap.objects.order_by('number')
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
    form_class = BeerUpdateForm
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
    """Ajax callback for when a beer is selected, so that the
        estimated values for OG, FG, IBU, SRM can be filled in."""
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
    """Return an RSS feed of the current tap pourings"""
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
    """Return an ATOM feed of the current tap pourings
        -- subclassed from RssTapFeed"""
    feed_type = Atom1Feed
    subtitle = RssTapFeed.description
