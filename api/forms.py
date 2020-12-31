from django import forms
from .models import Post,Client,Vendor,Match,NumberOfPhases
from django.forms.models import inlineformset_factory
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'
class VendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields='__all__'
class NumberOfPhasesForm(forms.ModelForm):
    class Meta:
        model=NumberOfPhases
        fields='__all__'
NumberOfPhasesInlineForm=inlineformset_factory(Match,NumberOfPhases,form=NumberOfPhasesForm,fields=['macth','phase','description','timeline','payments'],extra=1)