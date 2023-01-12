from django import forms
from .models import ContactLog
from django.utils.timezone import now

class ContactLogForm(forms.ModelForm):
    class Meta:
        model= ContactLog
        fields =['next_contact', 'actions', 'result']
        widgets={
            'next_contact': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date',
                'setdefault': now().strftime('%Y-%m-%d')

              })
        }