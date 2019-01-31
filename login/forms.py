from django import forms

class HandsForm(forms.Form):
	hands_cnt = forms.IntegerField(label='Hands Count', required=False)
	hrs_cnt = forms.IntegerField(label='Hours Count', required=False)