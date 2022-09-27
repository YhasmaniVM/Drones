from django.db import models
from decimal import Decimal
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models import ForeignKey

CUSTOM_NAME = RegexValidator(r'[0-9a-zA-Z-_]', 'Only letters, numbers, and underscores are allowed') #fix this
CUSTOM_CODE = RegexValidator(r'[0-9A-Z_]', 'Only upper-case letters, numbers, and underscore are allowed')
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Medication(models.Model):
    name = models.CharField(max_length=32, validators=[CUSTOM_NAME])
    weight = models.IntegerField(null=True)
    code = models.CharField(max_length=32, validators=[CUSTOM_CODE])
    image = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.name


class Drones(models.Model):
    MODELS = (
        ('lightweight', 'Lightweight'),
        ('middleweight', 'Middleweight'),
        ('cruiserweight', 'Cruiserweight'),
        ('heavyweight', 'Heavyweight'),
    )
    STATE = (
        ('idle', 'IDLE'),
        ('loading', 'LOADING'),
        ('loaded', 'LOADED'),
        ('delivering', 'DELIVERING'),
        ('delivered', 'DELIVERED'),
        ('returning', 'RETURNING'),
    )
    serial_number = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=32, null=True, choices=MODELS)
    weight = models.IntegerField(null=True, validators=[MaxValueValidator(500)])
    battery = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
    state = models.CharField(max_length=32, default='idle', choices=STATE)
    medications = models.ManyToManyField(Medication, blank=True)

    def __str__(self):
        return self.serial_number + ' - ' + self.model
