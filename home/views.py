from django.shortcuts import render
# from django.http import HttpResponse
from .forms import FormF
import numpy as np
import pickle

with open('home/data/DTPrun_model.pkl', 'rb') as fp:
    model = pickle.load(fp)


def inputs(saves, comments, shares, like, profile_visits, follow):
    features = np.array([[saves, comments, shares, like, profile_visits, follow]])
    # return features
    pred = model.predict(features)[0]
    return pred


def prediction(r):
    if r.method == 'POST':
        form = FormF(r.POST)
        if form.is_valid():
            saves = form.cleaned_data['saves']
            comments = form.cleaned_data['comments']
            shares = form.cleaned_data['shares']
            like = form.cleaned_data['like']
            profile_visits = form.cleaned_data['profile_visits']
            follow = form.cleaned_data['follow']
            pre = inputs(saves, comments, shares, like, profile_visits, follow)
            return render(r, 'home/home.html', {'pre': pre})
    else:
        form = FormF()
        return render(r, 'home/form.html', {'form': form})
