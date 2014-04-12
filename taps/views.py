from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import FormMessagesMixin
from braces.views import LoginRequiredMixin

from .forms import TapListForm
from .models import Tap


class TapList(ListView):
    """List of Taps"""
    model = Tap


class TapUpdate(LoginRequiredMixin,  FormMessagesMixin, UpdateView):
    """Update an existing keg
    """
    model = Tap
    form_class = TapListForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tap_list')
    form_valid_message = _(u"Tap was updated.")
    form_invalid_message = _(u"Something went wrong, tap was not updated.")

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
