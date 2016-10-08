from django.conf.urls import include, url
from django.contrib import admin
from signatures.views import generate_new_signature, home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^new_signature/(?P<optional>.*)/$', generate_new_signature, name='new_signature'),
    url(r'^new_signature/$', generate_new_signature, name='new_signature'),
]
