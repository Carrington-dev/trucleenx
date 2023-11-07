from django.forms import ModelForm

from django import forms
from django.core.exceptions import ValidationError

from book.models import Order
from book.variables import TIMES2

class OrderForm1(ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Order
        fields = ['first_name', "last_name", 'email']
      

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your surname'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
		
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
 
class OrderForm2(ModelForm):
    # appointed_date = forms.DateField()
    from_time = forms.CharField(max_length=300)

    class Meta:
        model = Order
        fields = ['city','from_time','appointed_date',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({'placeholder': 'Enter your city', "id": "city_id"})
        self.fields['from_time'].widget.attrs.update({'placeholder': 'Appointed starting time e.g 6:00 am to 7.00 am', "id": "from_id"})
        # self.fields['to_time'].widget.attrs.update({'placeholder': 'Enter your appointed starting time'})
        self.fields['appointed_date'].widget.attrs.update({'placeholder': 'Enter your appointed date yyyy-mm-dd', "type": "date"})
		
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    def clean(self):
 
        super(OrderForm2, self).clean()
         
        from_time = self.cleaned_data.get('from_time')
        
        if from_time not in TIMES2:
            raise ValidationError("Time should be part of the given list")
 
        if len(from_time) < 5:
            self._errors['from_time'] = self.error_class([
                'Minimum 5 characters required'])
        if from_time not in TIMES2:
            self._errors['from_time'] = self.error_class([
                'Time should be part of the given list'])
 
        return self.cleaned_data
 