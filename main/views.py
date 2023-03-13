from django.shortcuts import render, redirect
from .forms import ApplicationForm, ReviewForm
from .models import GAGAGA, Review
from captcha.fields import ReCaptchaField


def index(request):
    img = GAGAGA.objects.all()
    rev = Review.objects.all()

    if request.method == 'POST':
        captcha = ReCaptchaField(request.POST)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplicationForm()
        captcha = ReCaptchaField()
    if request.method == 'POST':
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            return redirect('home')
    else:
        review = ReviewForm()

    context = {'img': img, 'rev': rev, 'form': form, 'review': review}
    return render(request, 'main/home.html', context)


# def form(request):
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request, "main/index.html", {'form': form})
