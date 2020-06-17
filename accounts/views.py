from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from filebrowser.mixins import LoginRequiredMixin, AjaxRequiredMixin
from .mixins import AccountUpdateFormMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import View
from django.views.generic.edit import FormMixin
from accounts.models import UserProfile
from .decorators import student_required
from .forms import (
                SignUpForm, 
                ChangePasswordForm, 
                DeleteAccountPasswordForm, 
                UserProfileUpdateForm
                ) 
from .models import User

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SignUpView, self).get_context_data(*args, **kwargs)
        user = get_object_or_404(UserProfile, user=self.request.user)
        context['user'] = user
        return context

    def form_valid(self, form):
        user = form.save()
        return redirect('login')

class IndexView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = 'filemanager:browser'
            if request.user.is_superuser or request.user.is_staff:
                return redirect(profile)
            else:
                logout(request)
        return HttpResponseRedirect("/accounts/login/")

class UserProfileView(LoginRequiredMixin, AccountUpdateFormMixin, FormMixin, View):

    def get_form(self, *args, **kwargs):
        form = self.get_user_form()
        return form

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserProfile, user=self.request.user)
        user_form = self.get_form()
        profile_form = UserProfileUpdateForm()
       
        context = {}
        context["title"] = "User Profile"
        context['user'] = user
        context["user_form"] = user_form
        context["form"] = profile_form
        return render(request, "accounts/user_profile.html", context)

class UserAccountUpdateAjaxView(AjaxRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logged_in_user = request.user
        user_obj = get_object_or_404(User, username__iexact=logged_in_user.username)
        user_profile_obj = get_object_or_404(UserProfile, user=logged_in_user)
        user_first_name = request.GET.get("first_name")
        user_last_name = request.GET.get("last_name")
        user_email = request.GET.get('email')
        flash_message = ""
        if user_obj:
            user_obj.first_name = user_first_name
            user_obj.last_name = user_last_name
            user_obj.email = user_email
            user_obj.save()
            flash_message = "Profile successfully updated."
        data = {
            "flash_message": flash_message,
        }
        return JsonResponse(data, status=200)


class ChangePasswordView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserProfile, user=self.request.user)
        form = ChangePasswordForm()
       
        context = {}
        context["title"] = "Please change password"
        context['user'] = user
        context["form"] = form
        return render(request, "accounts/change-password.html", context)

class ChangePasswordAjaxView(AjaxRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        password1 = request.GET.get("password1")
        password2 = request.GET.get("password2")
        flash_message = ""
        try:
            if password1 and password2 and password1 != password2:
                flash_message = "Passwords don't match"
            user.set_password(password2)
            user.save()
            flash_message = "Password changed successfully"
            json_data = {
            "flash_message": flash_message,
            }
        except:
            json_data = {
                "flash_message": flash_message,
                }
        return JsonResponse(json_data, status=200)


class DeleteAccountView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserProfile, user=self.request.user)
        form = DeleteAccountPasswordForm()
       
        context = {}
        context["title"] = "Please change password"
        context['user'] = user
        context["form"] = form
        return render(request, "accounts/delete_account.html", context)


class UserAccountDeleteAjaxView(View):
    model = User

    def get_object(self, *args, **kwargs):
        user = self.request.user
        return user

    def get(self, request, *args, **kwargs):
        account = self.get_object()
        account_password = request.user.password
        password = request.GET.get("password")
        hashed_password = account.check_password(password)
        if hashed_password:
            account.delete()
            messages.success(request, 
                "Your account has been successfully deleted your, feel free to create an account with us anytime."
                )
        else:
            logout(request)
            messages.error(request, 
                "Permission denied, We've logged you out. Forgot your password?, try resetting it."
                )
        return redirect("/")