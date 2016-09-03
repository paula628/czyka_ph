from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'czyka_ph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'', include('core.urls', namespace='core')),
]

urlpatterns += static(settings.TEMP_URL, document_root=settings.MEDIA_ROOT)
