from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .forms import ContactForm


# Create your views here.
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection(
                'django.core.mail.backends.console.EmailBackend')
            send_mail(cd['subject'], cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'], connection=con)
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html', {'form': form,
                                            'submitted': submitted})
