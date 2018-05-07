from django.db import models
from django.conf import settings

class Ship(models.Model):
        VESSEL_CHOICES = (
                ('C', 'Cruisers'),
                ('D', 'Destroyers'),
                ('M', 'Minesweepers'),
                ('A', 'Anti-submarine'),
            )

        total_engaged = models.IntegerField(null=True)
        sunk = models.IntegerField(null=True)
        damaged = models.IntegerField(null=True)
        vessel = models.CharField(max_length=1, choices=VESSEL_CHOICES, blank=True)
        note = models.TextField(max_length=500, help_text="Any information on demand", blank=True)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

        def __str__(self):
            return self.vessel[:1]