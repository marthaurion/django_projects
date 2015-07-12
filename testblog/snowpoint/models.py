from django.db import models
from django.utils import timezone

# Create your models here.
class Participant(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class League(models.Model):
    ENTRY_TYPES = (
        ('C', 'Challenger'),
        ('G', 'Gym Leader'),
        ('E', 'Elite Four'),
    )
    name = models.CharField(max_length=50)
    participants = models.ManyToManyField(Participant)
    entry_type = models.CharField(max_length=1, choices=ENTRY_TYPES)

    def __str__(self):
        return self.name

class Match(models.Model):
    OUTCOMES = (
        (-1, 'Champion Win'),
        (0, 'Tie'),
        (1, 'Challenger Win'),
    )
    challenger = models.ForeignKey(Participant, related_name='challenger')
    champion = models.ForeignKey(Participant, related_name='champion')
    outcome = models.IntegerField(choices=OUTCOMES)
    match_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.challenger + " vs " + self.champion
