from django.shortcuts import render
from core.models import about_us, pricelist


def about_details_view(request, about_id):
    about = about_us.About.objects.get(id=about_id)
    price = pricelist.PriceList.objects.get()
    context = {
        'about': about, 
        'price': price
    }

    return render(request, 'about/about_details.html', context)
