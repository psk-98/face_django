from django.db import models

def upload_to(instance, filename):
    return '{name}/{filename}'.format(name=instance.user.name, filename=filename)


class User(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return f"{self.user.name}'s image"