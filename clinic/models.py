from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    MON = 1
    TUE = 2
    WEN = 3
    THU = 4
    FRI = 5 
    SAT = 6
    SUN = 7
    WEEKDAYS = (
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WEN, 'Wensday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday'),
    )

    weekdayFrom = models.IntegerField(choices=WEEKDAYS)
    weekdayTo = models.IntegerField(choices=WEEKDAYS)
    hourFrom = models.TimeField()
    hourTo = models.TimeField()
    
    def __str__(self):
        return 'гы'
        # return 'from ' + self.WEEKDAYS[self.weekdayFrom] + ' to ' + self.WEEKDAYS[self.weekdayTo]

class Doctor(models.Model):
    lastName = models.TextField('Фамилия')
    firstName = models.TextField('Имя')
    patronymic = models.TextField('Отчество')
    education = models.TextField('Образование')
    birthDate = models.DateField('Дата рождения')
    schedule = models.ForeignKey(Schedule)
    def __str__(self):
        return self.lastName + ' ' + self.firstName + ' ' + self.patronymic

class Holiday(models.Model):
    dateFrom = models.DateField()
    dateTo = models.DateField()
    hourFrom = models.TimeField()
    hourTo = models.TimeField()
    doctor = models.ForeignKey(Doctor)
    def __str__(self):
        return 'from ' + self.dateFrom + ' to ' + self.dateTo + ', from' + self.hourFrom + ' to ' + self.hourTo

class Patient(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    patronymic = models.TextField()
    birthDate = models.DateField()
    address = models.TextField()
    organization = models.TextField()
    position = models.TextField()

class Service(models.Model):
    cost = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.name
        
class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateField()
    hourFrom = models.TimeField()
    hourTo = models.TimeField()
    def __str__(self):
        return self.date + ', from ' + self.hourFrom + ' to ' + self.hourTo

class Comment(models.Model):
    service = models.ForeignKey(Service)
    content = models.TextField()
    pubDate = models.DateTimeField('date published', auto_now_add=True)
