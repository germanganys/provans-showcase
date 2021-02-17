from django.shortcuts import render
from core.forms import OrderForm
from core.utils import VKNotifier
from core.models import pricelist
from core.tasks import send_notification


def booking_view(request):
    booking_form = OrderForm(request.POST or None)
    price = pricelist.PriceList.objects.get()
    if request.POST and booking_form.is_valid():
        booking_form.save()
        msg = 'PROVANS! НОВАЯ ЗАПИСЬ\nИмя: {}\nТел: {}\n'.format(
                booking_form.cleaned_data.get('name'),
                booking_form.cleaned_data.get('phone_number')
        )

        send_notification.s(msg).delay()

        return render(request, 'booking/booking_success.html', {})

    context = {
        'booking_form': booking_form,
        'price': price
    }
    return render(request, 'booking/booking.html', context)
