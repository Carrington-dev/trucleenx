def show_me(request):
    context = {}
    context['company'] = "Trucleen"    
    context['country'] = "South Africa"    
    context['cc'] = "ZA"    
    context['state'] = "Gauteng"    
    context['city'] = "Pretoria"    
    context['contacts'] = ["+27 6765 0526 3", "+27 6765 0526 3" ]   
    context['zip'] = "0001"    
    context['street'] = "346 Thabo Sehume Street"    
    return context