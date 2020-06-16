from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ["__str__", "user", "profile_image", "active"]
	search_fields = ["user"]
	list_filter = ["user"]

	class Meta:
		model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)