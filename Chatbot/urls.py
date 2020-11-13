from django.contrib import admin
from django.urls import path, include
from madmin.views import *
from django.conf import settings
from django.conf.urls.static import static
# import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_login/', user_login, name="user_login"),
    path('user_logout/',user_logout, name='user_logout'),
    path('madmin/', include('madmin.urls')),
    path('magent/', include('magent.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
