from django.http import JsonResponse
from django.shortcuts import render

from core.models import promo, pricelist
from core.tasks import send_notification
from core.utils import generate_coupon_code


def promo_details_view(request, promo_id):
    _promo = promo.Promo.objects.get(id=promo_id)
    price = pricelist.PriceList.objects.get()
    context = {
        'promo': _promo,
        'price': price
    }

    return render(request, 'promo/promo_details.html', context)


def get_coupon(request):
    coupon = promo.DiscountCoupon()
    coupon.code = generate_coupon_code(5)
    coupon.save()

    msg = f'PROVANS! Получен купон: {coupon.code}'

    send_notification.s(msg).delay()

    return JsonResponse({
        'code': coupon.code
    })
