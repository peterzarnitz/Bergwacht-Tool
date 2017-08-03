from django import forms

from .models import nimmtTeilanDienst


class DienstTeilnahmeForm(forms.ModelForm):
    class Meta:
        model = nimmtTeilanDienst
        fields = ('von', 'bis', 'funktion', 'kommentar')
