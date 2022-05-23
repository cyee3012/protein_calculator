from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProteinForm(forms.Form):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.form_method = 'POST'
    self.helper.add_input(Submit('submit', 'calculate!'))

  SYSTEM_CHOICES = [("metric", "kgs"), ("imperial","lbs")]

  system = forms.CharField(label="Metric or Imperial?", widget=forms.Select(choices=SYSTEM_CHOICES))
  weight = forms.IntegerField()
