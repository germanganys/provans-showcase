from django.shortcuts import render


def robots_view(request):
    return render(None, 'etc/robots.txt', content_type='text/plain')


def sitemap_view(request):
    return render(None, 'etc/sitemap.xml', content_type='text/plain')
