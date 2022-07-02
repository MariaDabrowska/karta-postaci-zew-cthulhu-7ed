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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nazwa'].label = 'Imię Badacza'
        self.fields['nazwa'].widget.attrs.update({'placeholder': 'Jak Cię zwą?'})

        self.fields.pop('uzytkownik')


