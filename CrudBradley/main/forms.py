from django import forms


class CreateData(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    age = forms.IntegerField()
    gender = forms.IntegerField()
    contact = forms.IntegerField()
    amount = forms.IntegerField()
