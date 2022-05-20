from django import forms

SYSTEM_CHOICES = [("metric", "kgs"), ("imperial","lbs")]

class ProteinForm(forms.Form):
  system = forms.CharField(label="Metric or Imperial?", widget=forms.Select(choices=SYSTEM_CHOICES))
  weight = forms.CharField(label="Weight", max_length=3)
