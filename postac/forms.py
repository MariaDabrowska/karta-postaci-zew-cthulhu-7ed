from counter_widgets import CounterWidget
from django import forms

from postac.models import Postac


class FormPostac(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    wiek = forms.IntegerField(widget=CounterWidget)

    class Meta:
        model = Postac
        fields = '__all__'

