from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    longitude = models.FloatField(
        help_text=_('Longitude'),
    )

    latitude = models.FloatField(
        help_text=_('Latitude'),
    )

    squirrel_id = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=50,
        unique=True,
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    shift = models.CharField(
        help_text=_('Shift'),
        max_length=2,
        choices=SHIFT_CHOICES,
        default=AM,
    )

    date = models.DateField(
        help_text=_('Date'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'unknown'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        (UNKNOWN, 'unknown'),
    )

    age = models.CharField(
        help_text=_('Age'),
        max_length=16,
        choices=AGE_CHOICES,
        default=UNKNOWN,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (UNKNOWN, 'unknown'),
    )

    fur_color = models.CharField(
        help_text=_('Primary Fur Color'),
        max_length=50,
        choices=COLOR_CHOICES,
        default=UNKNOWN,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
        (UNKNOWN, 'unknown'),
    )

    location = models.CharField(
        help_text=_('Location'),
        max_length=50,
        choices=LOCATION_CHOICES,
        default=UNKNOWN,
    )

    specific_location = models.CharField(
        help_text=_('Specific Location'),
        max_length=100,
        blank=True,
    )

    running = models.BooleanField(
        help_text=_('Whether the squirrel is running'),
        default=False,
    )

    chasing = models.BooleanField(
        help_text=_('whether the squirrel is chasing'),
        default=False,
    )

    climbing = models.BooleanField(
        help_text=_('whether the squirrel is climbing'),
        default=False,
    )

    eating = models.BooleanField(
        help_text=_('whether the squirrel is eating'),
        default=False,
    )

    foraging = models.BooleanField(
        help_text=_('whether the squirrel is foraging'),
        default=False,
    )

    other_activities = models.CharField(
        help_text=_('Other actions of squirrel besides running, chasing, climbing, eating and foraging'),
        max_length=100,
        blank=True,
    )

    kuks = models.BooleanField(
        help_text=_('Whether the squirrel is in kuks'),
        default=False,
    )

    quaas = models.BooleanField(
        help_text=_('Whether the squirrel is in quaas'),
        default=False,
    )

    moans = models.BooleanField(
        help_text=_('Whether the squirrel is in moans'),
        default=False,
    )

    tail_flags = models.BooleanField(
        help_text=_('Whether the squirrel has tail flags'),
        default=False,
    )

    tail_twitches = models.BooleanField(
        help_text=_('Whether the squirrel has tail twitches'),
        default=False,
    )

    approaches = models.BooleanField(
        help_text=_('Whether the squirrel approaches human or not'),
        default=False,
    )

    indifferent = models.BooleanField(
        help_text=_('Whether the squirrel is indifferent or not'),
        default=False,
    )

    runs_from = models.BooleanField(
        help_text=_('Whether the squirrel runs from human or not'),
        default=False,
    )

    def __str__(self):
        return self.squirrel_id
