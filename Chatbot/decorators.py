from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied

def allowed_user(allowed_roles=[]):
	def decorator(func):
		def wrap(request, *args, **kwargs):
			if request.user.custom_user_model.urole in allowed_roles:
				return func(request, *args, **kwargs)
			else:
				raise PermissionDenied
		return wrap	
	return decorator	
	

def admin_only(view_func):
	def wrap(request, *args, **kwargs):
		if request.user.custom_user_model.urole=='1':
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponseRedirect(reverse('magent_dashboard'))
	return wrap