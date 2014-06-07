from django.db import models

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateTimeField('Race Date')

class Event(models.Model):
    name = models.CharField(max_length=200)
    distanceInKilometers = models.IntegerField()

class RaceEvent(models.Model):
    # a race can have many events
    # same event could belong to multiple races
    race = models.ForeignKey(Race)
    event = models.ForeignKey(Event)

class Runner(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s, %s' % (self.lastName, self.firstName)

class RaceResult(models.Model):
    runner = models.ForeignKey(Runner)
    raceEvent = models.ForeignKey(RaceEvent)
