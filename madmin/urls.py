from django.urls import path
from .views import *
from madmin.api_based_view import username_email_collection
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('user_signup/', user_signup, name='user_signup'),
	path('<bname>/madmin_dashboard/',madmin_dashboard, name='madmin_dashboard'),
	path('<bname>/teammates/', teammates, name='teammates'),
	path('<bname>/chat_widget/', chat_widget, name='chat_widget'),
	path('<bname>/user_data/', user_data, name='user_data'),
	path('username_email_collection/', username_email_collection, name='username_email_collection'),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)