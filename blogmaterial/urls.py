from django.conf.urls import include, url
from django.contrib import admin
from material.frontend import urls as frontend_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'myfirstblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
