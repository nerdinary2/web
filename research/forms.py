from django import forms


class HomeForm(forms.Form):
	merge = forms.CharField(required=False)
	delete = forms.CharField(required=False)
	check = forms.CharField(required=False)