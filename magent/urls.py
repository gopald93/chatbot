from django.urls import path
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('<bname>/conversation/',conversation, name='conversation'),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)