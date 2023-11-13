from django import forms

class Reg_form(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    user=forms.CharField()
    pwd=forms.CharField()
    cpwd=forms.CharField()
    





    