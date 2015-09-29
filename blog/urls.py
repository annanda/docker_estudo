"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
# from wagtail.wagtailimages import urls as wagtailimages_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^images/', include(wagtailimages_urls)),
    url(r'', include('puput.urls')),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()  # tell gunicorn where static files are in dev mode
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += patterns(
        '',
        (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'blog/images/favicon.ico'))
    )
