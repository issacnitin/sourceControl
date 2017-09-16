from django import forms

class WhatUserWants(forms.Form):
    language = forms.CharField(max_length=200)

    
    
