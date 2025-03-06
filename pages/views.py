from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        #validate data and send email
        form = ContactForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(f"Sending email From {email} with message: {message} from {username}")

            # message_body = render_to_string('pages/contact.html', request.POST)
            send_mail(subject, message, email, ['heffcontact@gmail.com'])
            print({email})
    else:
       form = ContactForm(initial={
           'username': request.user.username,
           'email': request.user.email,
        })

    return render(request, 'pages/contact.html', {'form': form})