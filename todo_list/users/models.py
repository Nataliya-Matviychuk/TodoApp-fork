from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='1.png', upload_to='profile_avatars')

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        """
        Handles customized save operation for the model to process the avatar image.

        This method overrides the default save operation to resize the avatar image if
        its dimensions exceed 300 pixels in either height or width. The avatar image
        is resized to a fixed output size of 200x200 pixels while maintaining its
        aspect ratio, and the resized image is saved back to its original path.

        Parameters:
            args: Variable positional arguments passed to the save method.
            kwargs: Variable keyword arguments passed to the save method.
        """
        super().save(*args, **kwargs)

        image = Image.open(self.avatar.path)

        if image.height > 300 or image.width > 300:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(self.avatar.path)
