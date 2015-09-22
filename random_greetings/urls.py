from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'signatures.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^new_signature/$', 'signatures.views.generate_new_signature', name='new_signature'),
]
