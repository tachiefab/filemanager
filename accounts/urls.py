from django.conf.urls import url
from .views import (
				IndexView, 
				SignUpView, 
				UserProfileView, 
				ChangePasswordView,
				DeleteAccountView
				)

app_name = "accounts"

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='home'),
    url(r'^add-user/$', SignUpView.as_view(), name='signup'),
    url(r'^change-password/$', ChangePasswordView.as_view(), name='change-password'),
    url(r'^delete-account/$', DeleteAccountView.as_view(), name='delete-account'),
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
   ]