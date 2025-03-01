from django.shortcuts import render
from django.views.generic import TemplateView
from. forms import ContactForm
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        #validate data and send email
        form = ContactForm(request.POST)

    
    else:
        form = ContactForm()

    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})