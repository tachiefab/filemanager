from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import ajax_required

class AjaxRequiredMixin(object):
	@method_decorator(ajax_required)
	def dispatch(self, request, *args, **kwargs):
		return super(AjaxRequiredMixin, self).dispatch(request, *args, **kwargs)

class StaffRequiredMixin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(StaffRequiredMixin, self).as_view(*args, **kwargs)
        return login_required(view)

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

