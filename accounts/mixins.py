from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .forms import UserUpdateForm

User = get_user_model()

class AccountUpdateFormMixin(object):

	def get_user_info(self, *args, **kwargs):
		user = get_object_or_404(User, username__iexact=self.request.user.username)
		first_name = user.first_name
		last_name =user.last_name
		email = user.email
		return first_name, last_name, email

	def get_user_form(self, *args, **kwargs):
		first_name, last_name, email = self.get_user_info()
		initial_data = {
		"first_name": first_name,
		"last_name": last_name,
		"email": email
		}
		user_form = UserUpdateForm(initial=initial_data)
		return user_form
