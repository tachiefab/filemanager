from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = get_user_model()


def upload_profile_image(instance, filename):
    return "profile/{username}/{filename}".format(username=instance.user.username, filename=filename)

class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image       = models.ImageField(upload_to=upload_profile_image, null=True, blank=True)
    active = models.BooleanField(default=True)

    objects = UserProfileManager()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        if first_name and last_name:
            return first_name + " " + last_name
        else:
            return self.user.username

    def get_user_level(self):
        is_admin = self.user.is_superuser
        is_staff = self.user.is_staff
        if is_admin and is_staff:
            return 'Administrator'
        else:
            return 'Staff'


    def get_profile_image_url(self):
        try:
            image = self.profile_image.url
        except:
            image = '/static/assets/img/profile-img.png'
        return image

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)
post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)
