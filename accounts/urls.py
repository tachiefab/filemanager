from django.conf.urls import url
from .views import (
				IndexView, 
				SignUpView, 
				UserProfileView, 
				ChangePasswordView,
				DeleteAccountView,
				UserAccountDeleteAjaxView,
				UserAccountUpdateAjaxView,
				ChangePasswordAjaxView
				)

app_name = "accounts"

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='home'),
    url(r'^add-user/$', SignUpView.as_view(), name='signup'),
    url(r'^change-password/$', ChangePasswordView.as_view(), name='change-password'),
    url(r'^delete-account/$', DeleteAccountView.as_view(), name='delete-account'),
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'^profile/delete/$', UserAccountDeleteAjaxView.as_view(), name='delete'),
    url(r'^profile/update/$', UserAccountUpdateAjaxView.as_view(), name='profile_update'),
    url(r'^password/change/$', ChangePasswordAjaxView.as_view(), name='password_change'),
   ]