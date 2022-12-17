from django import forms
from .models import *

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.fields:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.city_set
