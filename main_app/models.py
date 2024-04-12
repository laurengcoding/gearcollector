from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SERVICED = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

STATES = (
    ('NSW', 'New South Wales'),
    ('VIC', 'Victoria'),
    ('QLD', 'Queensland'),
    ('SA', 'South Australia'),
    ('WA', 'Western Australia'),
    ('ACT', 'Australian Capital Territory'),
    ('NT', 'Northern Territory'),
    ('TAS', 'Tasmania')
)

class Gig(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=256)
    state = models.CharField(
        max_length=3,
        choices=STATES,
        default=STATES[0][0],
    )
    city = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('gigs_detail', kwargs={'pk': self.id})
    
    def __str__(self):
        return self.name

class Gear(models.Model):
    brand = models.CharField(max_length=256)
    make = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    colour = models.CharField(max_length=256)
    gigs = models.ManyToManyField(Gig)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gear_id': self.id})

    def __str__(self):
        return f"{self.type} ({self.id})"

class Serviced(models.Model):
    date = models.DateField()
    serviced = models.CharField(
        max_length=1,
        choices=SERVICED,
        default=SERVICED[0][0],
    )
    g = models.ForeignKey(Gear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_serviced_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']