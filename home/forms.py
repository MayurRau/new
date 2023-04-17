from django import forms


class FormF(forms.Form):
    saves = forms.IntegerField()
    comments = forms.IntegerField()
    shares = forms.IntegerField()
    like = forms.IntegerField()
    profile_visits = forms.IntegerField()
    follow = forms.IntegerField()
