# from email.message import EmailMessage
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from contact.forms import ContactForm, SubscribeForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from contact.models import Contact, Subscribe
from trucleen import settings
from django.template.loader import render_to_string, get_template

def contact(request):
    context = {
        "title":"Contact"
    }
   
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
       
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request, 'Your information has been submitted')
            subject = "Trucleen Platform"
            to = ['crn96m@gmail.com']
            from_email = settings.DEFAULT_FROM_EMAIL
            contact_link = request.scheme + "://" + request.META['HTTP_HOST'] + "/admin"
            w_link = request.scheme + "://" + request.META['HTTP_HOST']
            # print(contact_link)

            ctx = {
                'c_link':contact_link,
                'w_link':w_link,
                'email': email, 
                'subject': subject, 
                'name': name, 
                'message': message, 
            }

            message = get_template('book/contact_email.html').render(ctx)
            # message = get_template('all/email.html').render(Context(ctx))
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
            return redirect('contact')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            # messages.error(request, "Your information was not submitted!.")
        
   
    else:
        form = ContactForm()
    context["form"] = form
    return render(request, "basic/contact.html", context)

def subcribe(request):
    context = {"title":"Subscribe" }
    form = SubscribeForm()
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            p = form.save()
            messages.success(request, "You have successfully subscribed to our newsletters!.")
            return redirect("home")
        else:
            messages.error(request, "Email address already taken, please use a different one!.")
            

    context['form'] = form
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    