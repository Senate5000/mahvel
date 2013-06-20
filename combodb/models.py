from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

class Character(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=255, blank=False, null=False)

class Ability(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=255, blank=False, null=False)
    inputs = models.CharField(max_length=255, blank=False, null=False)

class Combo(models.Model):
    character = models.ForeignKey(Character)
    inputs = models.TextField(blank=False, null=False)
    damage = models.CharField(max_length=255, blank=False, null=False)

# Create your models here.
class Feedback(models.Model):
    name = models.ForeignKey(Employee)
    timeframe_start = models.DateField(auto_now=False)
    timeframe_stop = models.DateField(auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=False, null=False)

    def __unicode__(self):
        return smart_unicode(self.id)
