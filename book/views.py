from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from book.forms import OrderForm1, OrderForm2
from book.models import Order
from book.variables import TIMES2
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from contact.forms import ContactForm, SubscribeForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from trucleen import settings
from django.template.loader import render_to_string, get_template

def book(request):
    context = dict()
    context['title'] = 'Booking | Cleaning Services'
    
    context['form2'] = OrderForm2()
    if request.method == 'POST':
        form = OrderForm1(request.POST)
        if form.is_valid():
            id = form.save()
            request.session['order_id'] = id.id
            return redirect('book_second')
    else:
        form = OrderForm1()
    context['form'] = form
    return render(request, "book/book_first.html", context)

def book_second(request):
    context = dict()
    context['title'] = 'Booking | Cleaning Services'
    
    context['form2'] = OrderForm2()
    if request.method == 'POST':
        form = OrderForm2(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            from_time = form.cleaned_data['from_time']
            appointed_date = form.cleaned_data['appointed_date']
            id = request.session['order_id']
            all_other = Order.objects.filter(appointed_date=appointed_date)
            aa =  { d.from_time for d in all_other }
            a = True if from_time in aa else False
            if a:
                messages.error(request, "This slot is already booked on this day please try a different time slot!.")
                redirect("book_second")
            else:
                order = Order.objects.get(id=id)
                order.city = city
                order.from_time = from_time
                order.appointed_date = appointed_date
                order.save()
                subject = "Trucleen Platform"
                # to = ['crn96m@gmail.com']
                to = [ order.email ]
                from_email = settings.DEFAULT_FROM_EMAIL
                contact_link = request.scheme + "://" + request.META['HTTP_HOST'] + "/admin"
                w_link = request.scheme + "://" + request.META['HTTP_HOST']

                ctx = {
                    'c_link':contact_link,
                    'w_link':w_link,
                    'email': order.email, 
                    'subject': subject, 
                    'name': order.first_name, 
                    'order': order, 
                }

                message = get_template('book/book_confirm.html').render(ctx)
                # message = get_template('all/email.html').render(Context(ctx))
                messages.success(request, "Your information was submitted, be sure to check your email.")
                msg = EmailMessage(subject, message, to=to, from_email=from_email)
                msg.content_subtype = 'html'
                msg.send()
                return redirect('done')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = OrderForm2()
    context['form'] = form
    return render(request, "book/book_second.html", context)

def autocomplete(request):
    if 'term' in request.GET:
        qs = ["Johannesburg", "Vereeniging", "Pietermaritzburg", "Pretoria", "Durban", "Cape Town", "Welkom", "East London", "Randburg", "Roodepoort", "Port Elizabeth", "Bloemfontein", "Centurion", "Springs", "Sandton", "Polokwane", "Klerksdorp", "Rustenburg", "Kimberley", "Bhisho", "Benoni", "George", "Middelburg", "Vryheid", "Potchefstroom", "Umtata", "Brits", "Alberton", "Upington", "Paarl", "Queenstown", "Mmabatho", "Kroonstad", "Uitenhage", "Bethal", "Worcester", "Vanderbijlpark", "Grahamstown", "Standerton", "Brakpan", "Thohoyandou", "Saldanha", "Tzaneen", "Graaff-Reinet", "Oudtshoorn", "Mossel Bay", "Port Shepstone", "Knysna", "Vryburg", "Ladysmith", "Kuilsrivier", "Beaufort West", "Aliwal North", "Volksrust", "Musina", "Vredenburg", "Malmesbury", "Lebowakgomo", "Cradock", "De Aar", "Ulundi", "Jeffrey's Bay", "Lichtenburg", "Hermanus", "Carletonville", "Mahikeng", "Nelspruit"]
        # qs = Product.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            if product.lower().__contains__(request.GET.get('term').lower()) or request.GET.get('term').strip() in product.lower():
                titles.append(product)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'basic/home.html')


def autocomplete2(request):
    if 'term' in request.GET:
        qs = TIMES2
        # qs = Product.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            if product.lower().__contains__(request.GET.get('term').lower()):
                titles.append(product)
        return JsonResponse(titles, safe=False)
    return render(request, 'basic/home.html')


def done(request):
    return render(request, "book/done.html", {"title":"Booking was successfully"})