from django import forms
from models import Tap, Beer

class TapListForm(forms.ModelForm):

    number = forms.IntegerField(
            widget=forms.TextInput(
                    attrs={'readonly':'readonly', 'class':'tapcircle'})
        )

    class Meta:
        model = Tap
        fields = [ 'number', 'active', 'keg', 'beer', 'ogAct', 'fgAct',
                    'srmAct', 'ibuAct' ]
