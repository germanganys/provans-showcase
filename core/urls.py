from django.conf.urls import url
from django.views.generic import RedirectView
from core.views import main, service, booking, etc, promo, about


urlpatterns = [
    url(r'^$', main.main_view, name='main_page'),

    url(r'^service/(?P<service_id>[-\w+]+)/$', service.service_details_view, name='service_details_page'),

    url(r'^about/(?P<about_id>[-\w+]+)/$', about.about_details_view, name='about_details_page'),

    url(r'^booking/$', booking.booking_view, name='booking_page'),

    url(r'^promo/(?P<promo_id>[-\w+]+)/$', promo.promo_details_view, name='promo_details_page'),
    url(r'^get-coupon/$', promo.get_coupon, name='get-coupon'),

    url(r'^sitemap.xml$', etc.sitemap_view),
    url(r'^robots.txt$', etc.robots_view),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/imgs/favicon.ico'), name='favicon'),
]

handler404 = 'core.views.errors.error404_view'
handler500 = 'core.views.errors.error500_view'
