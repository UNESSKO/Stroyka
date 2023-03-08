from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicationForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>XUI</h4>")


def form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')