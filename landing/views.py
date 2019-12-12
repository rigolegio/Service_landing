from django.shortcuts import render
from .forms import SubscriberForm

# Create your views here.
def landing(request):
    form = SubscriberForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        data = form.cleaned_data
        print(data)

        new_form = form.save()
    return render(request, 'landing\index.html', locals())
