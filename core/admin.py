from django.contrib import admin
from core.models import service, order, portfolio, promo, about_us, pricelist


class ServiceModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ServiceModelAdmin, self).get_queryset(request)
        return qs.order_by("service_type", "sort_priority")


admin.site.site_header = 'Provans!'
admin.site.register(service.Service, ServiceModelAdmin)
admin.site.register(order.Order)
admin.site.register(portfolio.PortfolioPhoto)
admin.site.register(promo.Promo)
admin.site.register(promo.DiscountCoupon)
admin.site.register(about_us.About)
admin.site.register(pricelist.PriceList)
