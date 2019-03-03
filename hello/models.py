from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Room(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    when = models.DateTimeField(auto_now_add=True, verbose_name=b'date created')
    host = models.CharField(max_length=30)
    starting_chips = models.IntegerField()
    pot = models.IntegerField()

class Player(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='identification_number')
    when = models.DateTimeField(auto_now_add=True, verbose_name=b'date created')
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    chips = models.IntegerField()
    last_bet = models.IntegerField()
