from django.shortcuts import render
from .forms import Imageform
from .models import Image

# Create your views here.

def home(request):
    if request.method == "POST":
        forms = Imageform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
    forms = Imageform()
    img = Image.objects.all()
    return render(request, "myapp/Template/home.html", {'img':img, 'form':forms})
