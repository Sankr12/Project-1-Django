from django import forms

class userForms(forms.Form):
    name=forms.CharField(label="value1", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    contact=forms.CharField(label="value2", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    people=forms.CharField(label="value3", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    message=forms.CharField(label="value4", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))