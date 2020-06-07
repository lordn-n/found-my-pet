from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    last_names = models.CharField(max_length=200, blank=False, null=False)
    phone = PhoneField(blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    address = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.name} {self.last_names}'


class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    species = models.CharField(max_length=200, blank=False, null=False)
    breed = models.CharField(max_length=200, blank=False, null=False)
    color = models.CharField(max_length=200, blank=False, null=False)
    photo = models.ImageField(upload_to='static/pets_photos', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    lost = models.BooleanField(default=False, blank=False, null=False)
    lost_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        lost = ''
        if self.lost is True:
            lost = '[PERDIDO] '

        return f'{lost}{self.name} de {self.owner} ({self.species} / {self.breed} / {self.color})'


class Report(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=False, null=False)
    location = models.CharField(max_length=200)
    information = models.TextField()
