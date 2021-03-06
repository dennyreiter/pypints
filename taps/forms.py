from django import forms
from django.db.models import Q

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, Submit, MultiField
from crispy_forms.bootstrap import FormActions, InlineRadios

#from beers.models import Beer
from .models import Tap
from kegs.models import Keg
from beers.models import Beer

class TapListForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
            super(TapListForm, self).__init__(*args, **kwargs)
            #self.fields['keg'].queryset = Keg.objects.exclude(kegstatus__in=('SERVING','NEEDS_PARTS','NEEDS_REPAIRS','NEEDS_CLEANING'))
            self.fields['keg'].queryset = Keg.objects.filter(Q(active=True),
                    Q(pk=self.instance.keg_id) | ~Q(kegstatus__in=('SERVING','NEEDS_PARTS','NEEDS_REPAIRS','NEEDS_CLEANING'))
                    )
            self.fields['beer'].queryset = Beer.objects.filter(active=True)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-6'
            self.helper.layout = Layout(
                Field('number', readonly="readonly"),
                Field('active',),
                InlineRadios('tap_type'),
                Field('beer',),
                Field('keg',),
                MultiField("Gravities",
                    Field('og_actual',),
                    Field('fg_actual',),
                ),
                Field('srm_actual',),
                Field('ibu_actual',),
                FormActions(
                    Submit('save', 'Save changes'),
                    Button('cancel', 'Cancel'),
                    )
            )

    class Meta:
        model = Tap
