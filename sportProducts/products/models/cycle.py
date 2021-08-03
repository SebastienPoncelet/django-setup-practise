from django.db import models


class Cycle(models.Model):
    active_duration = models.IntegerField()
    inactive_duration = models.IntegerField()
    number_repetition = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "active: {} day(s), inactive: {} day(s), repeat: {} times".format(
            self.active_duration,
            self.inactive_duration,
            self.number_repetition
            )