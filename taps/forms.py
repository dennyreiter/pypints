from django import forms

#from beers.models import Beer
from .models import Tap

class TapListForm(forms.ModelForm):

    number = forms.IntegerField(
            widget=forms.TextInput(
                    attrs={'readonly':'readonly', 'class':'tapcircle'})
        )

    class Meta:
        model = Tap
        fields = [ 'number', 'active', 'keg', 'beer', 'og_actual', 'fg_actual',
                    'srm_actual', 'ibu_actual' ]

