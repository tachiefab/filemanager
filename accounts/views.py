from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from filebrowser.mixins import LoginRequiredMixin
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

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserProfile, user=self.request.user)
        user_form = self.get_user_form()
        profile_form = UserProfileUpdateForm()
       
        context = {}
        context["title"] = "User Profile"
        context['user'] = user
        context["user_form"] = user_form
        context["form"] = profile_form
        return render(request, "accounts/user_profile.html", context)


class ChangePasswordView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserProfile, user=self.request.user)
        form = ChangePasswordForm()
       
        context = {}
        context["title"] = "Please change password"
        context['user'] = user
        context["form"] = form
        return render(request, "accounts/change-password.html", context)


class DeleteAccountView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserProfile, user=self.request.user)
        form = DeleteAccountPasswordForm()
       
        context = {}
        context["title"] = "Please change password"
        context['user'] = user
        context["form"] = form
        return render(request, "accounts/delete_account.html", context)