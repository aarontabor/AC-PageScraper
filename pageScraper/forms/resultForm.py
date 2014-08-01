from django import forms

class ResultForm(forms.Form):
  position = forms.IntegerField()
  bib = forms.IntegerField()
  gunTime = forms.IntegerField()
  chipTime = forms.IntegerField(required=False)
  division = forms.IntegerField(required=False)
