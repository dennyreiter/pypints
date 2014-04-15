from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, Submit
from crispy_forms.bootstrap import FormActions, InlineRadios

from .models import Keg

class KegForm(forms.ModelForm):

    notes = forms.CharField(
        widget = forms.Textarea(),
        )

    def __init__(self, *args, **kwargs):
            super(KegForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-4'
            self.helper.layout = Layout(
            FormActions(
                Field('label', ),
                Field('kegtype',),
                InlineRadios('kegstatus'),
                Field('make',),
                Field('model',),
                Field('serial',),
                Field('stampedOwner',),
                Field('stampedLocation',),
                Field('notes', rows="3", css_class='input-xlarge'),
                Field('weight',),
                    )
            )

    class Meta:
        model = Keg

class KegCreateForm(KegForm):

    def __init__(self, *args, **kwargs):
            super(KegCreateForm, self).__init__(*args, **kwargs)
            self.helper.add_input( Submit('create', 'Create'))
            self.helper.add_input( Button('cancel', 'Cancel'))


class KegUpdateForm(KegForm):

    def __init__(self, *args, **kwargs):
            super(KegUpdateForm, self).__init__(*args, **kwargs)
            self.helper.add_input( Submit('update', 'Update'))
            self.helper.add_input( Button('cancel', 'Cancel'))

