from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, Submit
from crispy_forms.bootstrap import FormActions, InlineRadios

from .models import Beer


class BeerForm(forms.ModelForm):

    notes = forms.CharField(
        widget = forms.Textarea(),
        )
    
    def __init__(self, *args, **kwargs):
            super(BeerForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-4'
            self.helper.layout = Layout(
                Field('name', ),
                Field('style',),
                Field('notes', rows="7", css_class='input-xlarge'),
                Field('og_estimated',),
                Field('fg_estimated',),
                Field('srm_estimated',),
                Field('ibu_estimated',),
                Field('active',),
                FormActions(
                    )
            )


    class Meta:
        model = Beer
        fields = ['name', 'style', 'notes', 'srm_estimated', 'ibu_estimated',
                    'og_estimated', 'fg_estimated', 'active']


class BeerCreateForm(BeerForm):

    def __init__(self, *args, **kwargs):
        super(BeerCreateForm, self).__init__(*args, **kwargs)
        self.helper.add_input( Submit('create', 'Create'))
        self.helper.add_input( Button('cancel', 'Cancel'))

class BeerUpdateForm(BeerForm):

    def __init__(self, *args, **kwargs):
        super(BeerUpdateForm, self).__init__(*args, **kwargs)
        self.helper.add_input( Submit('update', 'Update'))
        self.helper.add_input( Button('cancel', 'Cancel'))

