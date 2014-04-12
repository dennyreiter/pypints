from django import forms
from .models import Beer


class BeerForm(forms.ModelForm):

    class Meta:
        model = Beer
        fields = ['name', 'style', 'notes', 'srm_estimated', 'ibu_estimated',
                    'og_estimated', 'fg_estimated', 'active']


class BeerUpdateForm(BeerForm):

    class Meta(BeerForm.Meta):
        fields = ['name', 'slug', 'style', 'notes', 'srm_estimated', 'ibu_estimated',
                    'og_estimated', 'fg_estimated', 'active']

