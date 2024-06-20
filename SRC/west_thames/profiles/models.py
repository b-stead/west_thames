from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Team(models.Model):
    name = models.CharField(_("name"), max_length=50)
    manager = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Rider(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    DIV_CHOICES = [
        ('0', 'Elite'),
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rds'),
        ('4', '4ths')
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    current_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_riders')
    current_division = models.CharField(max_length=1, choices=DIV_CHOICES)
    bc_num = models.IntegerField(unique=True)

    def __str__(self):
        return self.user.get_full_name()

class TeamMembership(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.rider} - {self.team} ({self.start_date} to {self.end_date or 'Present'})"

class Season(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return f"Season {self.year}"

class Event(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.season.year} ({self.date})"

class RaceCategory(models.Model):
    CATEGORY_CHOICES = [
        ('M_E123', 'Men E123'),
        ('M_3', 'Men 3rd'),
        ('M_4', 'Men 4th'),
        ('W_E123', 'Women E123'),
        ('W_34', 'Women 3/4'),
    ]
    
    name = models.CharField(max_length=10, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Race(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.ForeignKey(RaceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.name} - {self.category}"

class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    time = models.DurationField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.race} - {self.rider} - {self.team} - {self.position}"

    class Meta:
        unique_together = ('race', 'rider')

class SeasonPoints(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()

    class Meta:
        unique_together = ('season', 'rider')

    def __str__(self):
        return f"{self.season.year} - {self.rider} - {self.points} points"
