from django import forms


class PredictForm(forms.Form):

    name_of_company     = forms.CharField(label="Enter Company Ticker")
