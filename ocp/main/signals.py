from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist

CustomUser = get_user_model()

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
	try:
		instance.userprofile.save()
	except ObjectDoesNotExist:
		UserProfile.objects.create(user=instance)

