from django import forms

SYSTEM_CHOICES = [("kgs", "kgs"), ("lbs","lbs")]

class ProteinForm(forms.Form):
  system = forms.CharField(label="kgs or lbs?", widget=forms.Select(choices=SYSTEM_CHOICES))
  weight = forms.CharField(label="Weight", max_length=3)
