from django.db import models

# Create your models here.

class Event(models.Model):
    EVENT_TYPES = (
        ('financial', 'Financial'),
        ('fun', 'Fun'),
        ('accident', 'Accident'),
        ('payment', 'Payment'),
        ('life', 'Life')
    )
    event_name = models.CharField(max_length=120, default='')
    event_text = models.TextField()
    event_type = models.CharField(choices=EVENT_TYPES, default='financial', max_length=300)
    event_image = models.ImageField(upload_to='events', blank=True)
    event_background = models.ImageField(upload_to='events', blank=True)

    def __str__(self):
        return self.event_name

class Choice(models.Model):
    KARMA = (
        (0, 'Neutral karma'),
        (1, 'Good karma'),
        (-1, 'Bad karma'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120, default='')
    karma =  models.IntegerField(choices=KARMA, default=0)
    points = models.IntegerField(default=0)

class Odds(models.Model):
    VAR_TYPES = (
        ('age', 'Age'),
        ('education', 'Education'),
        ('child', 'Children'),
        ('sex', 'Sex'),
        ('income', 'Income'),
    )
    Choice = models.ForeignKey(Event, on_delete=models.CASCADE)
    variable_type = models.CharField(max_length=120, default='', choices=VAR_TYPES)
    variable_value = models.CharField(default='', max_length=12)
    variable_odds = models.FloatField(default=0)
