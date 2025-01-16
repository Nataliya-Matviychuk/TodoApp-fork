from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Handles the creation of a Profile instance associated with a newly created User.
    This function acts as a signal receiver connected to the post_save signal of the
    User model. When a new User is created, this function automatically creates a
    corresponding Profile instance linked to that User. It ensures that every User
    has an associated Profile.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    A signal receiver function that ensures the related user profile is saved
    automatically whenever the associated `User` object is saved. This simplifies
    the synchronization of user data and its profile whenever updates occur to the
    `User` model.
    This function does not return any value, as it operates for side-effects only
    by saving the related profile linked to the `User` model instance.
    """
    instance.profile.save()
