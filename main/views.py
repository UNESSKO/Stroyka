from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ApplicationForm, ReviewForm
from .models import GAGAGA
from captcha.fields import ReCaptchaField


def index(request):
    img = GAGAGA.objects.all()

    if request.method == 'POST':
        captcha = ReCaptchaField(request.POST)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApplicationForm()
        captcha = ReCaptchaField()

    if request.method == 'POST':
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
    else:
        review = ReviewForm()

    context = {'img': img, 'form': form, 'review': review}
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("<h4>XUI</h4>")


# def form(request):
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request, "main/index.html", {'form': form})
