from django import forms

from .fields import DateTimePickerField
from .models import nimmtTeilanDienst


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class DienstTeilnahmeForm(BootstrapModelForm):
    class Meta:
        model = nimmtTeilanDienst
        fields = ('von', 'bis', 'funktion', 'kommentar')
        field_classes = {
            'von': DateTimePickerField,
            'bis': DateTimePickerField,
        }

    def __init__(self, *args, **kwargs):
        super(DienstTeilnahmeForm, self).__init__(*args, **kwargs)
