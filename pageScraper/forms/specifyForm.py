from django import forms


class SpecifyForm(forms.Form):
  url = forms.CharField()
