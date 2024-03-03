from django.shortcuts import render
from . import models
from . import forms


def index(request):
    tasks = models.Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def about(request):
    self = models.About.objects.all()
    return render(request, 'about.html', {'self': self})


def blog(request):
    notes = models.Note.objects.all()
    return render(request, 'blog.html', {'notes': notes})

def contact_view(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = forms.ContactForm()
    context = {'form': form}
    return render(request, 'contacts.html', context)
