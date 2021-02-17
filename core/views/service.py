from django.shortcuts import render
from core.models import service, pricelist


def service_details_view(request, service_id):
    _service = service.Service.objects.get(id=service_id)
    price = pricelist.PriceList.objects.get()
    context = {
        'service': _service,
        'price': price
    }
    return render(request, 'service/service_details.html', context)
