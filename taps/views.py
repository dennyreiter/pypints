from django.conf import settings
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext as _
from django.views.generic import View
#from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from braces.views import FormMessagesMixin
from braces.views import LoginRequiredMixin

from .forms import TapListForm
from .models import Tap
from kegs.models import Keg


class TapList(ListView):
    """List of Taps"""
    model = Tap


class TapUpdate(LoginRequiredMixin,  FormMessagesMixin, UpdateView):
    """Update an existing tap
    """
    model = Tap
    form_class = TapListForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tap:list')
    form_valid_message = _(u"Tap was updated.")
    form_invalid_message = _(u"Something went wrong, tap was not updated.")

    raise_exception = False
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        keg = Keg.objects.get(pk=form.instance.keg_id)
        keg.kegstatus='SERVING'
        keg.save()
        return super(TapUpdate, self).form_valid(form)


class TapCount(LoginRequiredMixin, View):
    """Change the number of Taps that are on display
    """
    def post(self, request, *args, **kwargs):
        if self.request.POST.get('numberOfTaps'):
            newcount = int(self.request.POST.get('numberOfTaps'))
            current_taps = Tap.objects.count()
            if (current_taps > newcount):
                Tap.objects.filter(number__gt = newcount).delete()
            elif (current_taps < newcount):
                for x in range(current_taps+1, newcount+1):
                    tap = Tap.objects.create(number = x)
                    tap.save()

        return HttpResponseRedirect(reverse_lazy('tap:list'))


class TapChange(LoginRequiredMixin, View):
    """Make changes to the referenced tap, such as closing it
    """
    def post(self, request, *args, **kwargs):
        if self.request.POST.get('closeTap'):
            tap = Tap.objects.get(pk=int(self.request.POST.get('id')))
            keg = Keg.objects.get(pk=tap.keg.id)
            keg.kegstatus = 'NEEDS_CLEANING'
            keg.save()
            tap.og_actual =0
            tap.fg_actual = 0
            tap.srm_actual = 0
            tap.ibu_actual = 0
            tap.beer = None
            tap.keg = None
            tap.save()
        elif self.request.POST.get('newKeg') or self.request.POST.get('changeTap'):
            return HttpResponseRedirect(reverse('tap:update', 
                        kwargs = {'pk': self.request.POST.get('id')} ))

        return HttpResponseRedirect(reverse_lazy('tap:list'))


class RssTapFeed(Feed):
    """Return an RSS feed of the current tap pourings"""
    title = "PyPints Tap List"
    link = "/"
    description = "What's currently being poured."

    def items(self):
        return Tap.objects.exclude(beer__isnull=True).filter(active=True).order_by('number')

    def item_title(self, item):
        return unicode(item.beer.name)

    def item_description(self, item):
        return unicode(item.beer.notes)

    def item_link(self, item):
        return self.link


class AtomTapFeed(RssTapFeed):
    """Return an ATOM feed of the current tap pourings
        -- subclassed from RssTapFeed"""
    feed_type = Atom1Feed
    subtitle = RssTapFeed.description
