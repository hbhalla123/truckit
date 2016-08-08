from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from truck_order.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Truckde.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
url(r'^home/$', 'truck_order.views.home',name='home'),
url(r'^thanku/$', 'truck_order.views.thanks',name='thanks'),
url(r'^home/vehicle_info/$', 'truck_order.views.vehicle_info',name='vehicle_info'),
url(r'^home/add/$', 'truck_order.views.post_order',name='createAjax'),
url(r'^home/price/$', 'truck_order.views.price_add',name='price_add'),

#url(r'^home/$', 'truck_order.views.vehicles',name='vehicles'),
    url(r'^admin/', include(admin.site.urls)),
)
