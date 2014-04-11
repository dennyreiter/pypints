from django import forms
from .models import Tap, Beer

class TapListForm(forms.ModelForm):

    number = forms.IntegerField(
            widget=forms.TextInput(
                    attrs={'readonly':'readonly', 'class':'tapcircle'})
        )

    class Meta:
        model = Tap
        fields = [ 'number', 'active', 'keg', 'beer', 'ogAct', 'fgAct',
                    'srmAct', 'ibuAct' ]


class BeerForm(forms.ModelForm):

    class Meta:
        model = Beer
        fields = ['name', 'style', 'notes', 'srmEst', 'ibuEst',
                    'ogEst', 'fgEst', 'active']


class BeerUpdateForm(BeerForm):

    class Meta(BeerForm.Meta):
        fields = ['name', 'slug', 'style', 'notes', 'srmEst', 'ibuEst',
                    'ogEst', 'fgEst', 'active']

