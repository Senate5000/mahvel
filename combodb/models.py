from django.db import models
from django.utils.encoding import smart_unicode

class Game(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return smart_unicode(self.title)


class Character(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return smart_unicode(self.name)


class Ability(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=255, blank=False, null=False)
    inputs = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return smart_unicode(self.name)


class Combo(models.Model):
    character = models.ForeignKey(Character)
    inputs = models.TextField(blank=False, null=False)
    damage = models.CharField(max_length=255, blank=False, null=False)
    bar = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return smart_unicode(self.id)
