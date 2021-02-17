from django.forms import ModelForm, ValidationError
from core.models import order
from crispy_forms.helper import FormHelper
import re


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        super().__init__(*args, **kwargs)

    class Meta:
        model = order.Order
        fields = ['phone_number', 'name']

        labels = {
            'name': 'Имя:',
            'phone_number': 'Номер телефона:',
        }

    def clean(self):
        super().clean()
        phone_number = self.cleaned_data.get('phone_number')

        if not re.match(r'^\+7-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$', phone_number):
            raise ValidationError('Укажите корректный номер телефона')
        return self.cleaned_data

