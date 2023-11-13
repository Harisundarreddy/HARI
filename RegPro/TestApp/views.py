from django.shortcuts import render
from TestApp import forms

# Create your views here.
def Reg_view(request):
    frm=forms.Reg_form()
    return render(request,'testapp/home.html',{'FRM':frm})
