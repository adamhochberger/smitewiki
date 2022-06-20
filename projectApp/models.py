from django.db import models

from projectApp.utils.constants import ItemTypes


class Item:
    name = models.TextField(default="")
    stats = models.JSONField(default="")
    icon = models.ImageField(default=None)
    type = models.JSONField(default=ItemTypes.NEUTRAL)
    cost = models.PositiveSmallIntegerField(default=0)

    passive = models.TextField(default="")
    is_starter = models.BooleanField(default=False)


    previous_item = models.OneToOneField('self', on_delete=models.CASCADE)
    next_item = models.ForeignKey('self', on_delete=models.CASCADE)
