from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now())
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='ML')
    descriptions = models.TextField(default='')
    price = models.FloatField(default=0.0)
    def __str__(self):
        return self.name
    
# one to Many relationship model

class chaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.chai.name + " " + self.user.username + " " + str(self.date_added)

# many to many relationship

class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name
    
# one to one relationship
class certificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE,related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(timezone.now())
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.name.chai}"


