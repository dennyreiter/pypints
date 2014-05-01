from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView

from braces.views import FormMessagesMixin
from braces.views import LoginRequiredMixin

from .forms import  UserForm


def logout_page(request):
    """
        Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


class UserCreate(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a user
    """
    model = User
    success_url = reverse_lazy('dashboard')
    form_class = UserForm
    form_valid_message = _(u"User was created.")
    form_invalid_message = _(u"Something went wrong, user was not saved")

    template_name = 'registration/register.html'

    raise_exception = False
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super(UserCreate, self).form_valid(form)

