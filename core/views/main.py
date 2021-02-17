from django.shortcuts import render
from core.models import service, portfolio, promo, about_us, pricelist
from random import shuffle


def main_view(request):
    hair_services = service.Service.objects.filter(service_type='_hair').order_by("sort_priority")
    nail_services = service.Service.objects.filter(service_type='_nails').order_by("sort_priority")
    categories = service.ServiceCategory.objects.all()
    promos = promo.Promo.objects.all()

    portfolio_photos = list(portfolio.PortfolioPhoto.objects.all())
    shuffle(portfolio_photos)

    about = about_us.About.objects.all()
    price = pricelist.PriceList.objects.get()

    context = {
        'categories': categories,
        'promos': promos,
        'portfolio_photos': portfolio_photos,
        'hair_services': hair_services,
        'nail_services': nail_services,
        'about': about,
        'price': price
    }
    return render(request, 'main.html', context)
