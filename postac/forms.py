from django import forms

from postac.models import Postac, ZestawCechPostaci


class FormPostac(forms.ModelForm):
    # error_css_class = 'error-field'
    # required_css_class = 'required-field'

    ekwipunek = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40, 'style': 'height: 2em'}))
    historia = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40, 'style': 'height: 2em'}))
    uzbrojenie = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40, 'style': 'height: 2em'}))

    class Meta:
        model = Postac
        exclude = ['uzytkownik', ]
        help_texts = {
            'wiek': 'Kliknij w pole i użyj scrolla by wybrać wiek'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nazwa'].label = 'Imię Badacza'
        self.fields['nazwa'].widget.attrs.update({'placeholder': 'Jak Cię zwą?'})
        self.fields['um'].label = 'Lista umiejętności'
        # self.fields['cechy'].widget.attrs = forms.HiddenInput()


class FormZestawCech(forms.ModelForm):
    class Meta:
        model = ZestawCechPostaci
        exclude = '__all__'



