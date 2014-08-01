from django import forms

class RunnerForm(forms.Form):
  name = forms.IntegerField()
  sex = forms.IntegerField()
  city = forms.IntegerField(required=False)
  province = forms.IntegerField(required=False)
