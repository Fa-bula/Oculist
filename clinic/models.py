from django.db import models
from django.contrib.auth.models import User
import os

class Schedule(models.Model):
    MON = 1
    TUE = 2
    WEN = 3
    THU = 4
    FRI = 5 
    SAT = 6
    SUN = 7
    WEEKDAYS = (
        (MON, 'Понедельник'),
        (TUE, 'Вторник'),
        (WEN, 'Среда'),
        (THU, 'Четверг'),
        (FRI, 'Пятница'),
        (SAT, 'Суббота'),
        (SUN, 'Воскресенье'),
    )

    weekdayFrom = models.IntegerField(choices=WEEKDAYS)
    weekdayTo = models.IntegerField(choices=WEEKDAYS)
    hourFrom = models.TimeField()
    hourTo = models.TimeField()
    name = models.TextField()
    
    def __str__(self):
        return self.name

    def print(self):
        return self.WEEKDAYS[self.weekdayFrom - 1][1] + '-' + self.WEEKDAYS[self.weekdayTo - 1][1] + ', с ' + self.hourFrom.strftime('%H:%M') + ' до ' + self.hourTo.strftime('%H:%M')
    
class Doctor(models.Model):
    CAR = 1
    TER = 2
    DOCTOR_TYPES = (
        (CAR, 'Кардиолог'),
        (TER, 'Терапевт'),
    )

    doctorType = models.IntegerField('Специализация', choices=DOCTOR_TYPES)
    lastName = models.TextField('Фамилия')
    firstName = models.TextField('Имя')
    patronymic = models.TextField('Отчество')
    education = models.TextField('Образование')
    birthDate = models.DateField('Дата рождения')
    schedule = models.ForeignKey(Schedule)
    photo = models.FilePathField(path='/home/bulat/projects/Okulist/clinic/static/clinic/img/doctors/')

    def __str__(self):
        return self.lastName + ' ' + self.firstName + ' ' + self.patronymic

    def url(self):
        path = self._meta.get_field('photo').path
        return 'clinic/img/doctors/' + self.photo.replace(path, '', 1)
    
    def print_specialization(self):
        return self.DOCTOR_TYPES[self.doctorType - 1][1]
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
    description = models.TextField()
    doctor = models.ForeignKey(Doctor)
    VIS = 1
    MAS = 2
    SERVICE_TYPES = (  
        (VIS, 'Прием у врача'),
        (MAS, 'Массаж'),
    )
    serviceType = models.IntegerField(choices=SERVICE_TYPES)

    def __str__(self):
        return self.SERVICE_TYPES[self.serviceType - 1][1] + ' (' + self.doctor.__str__() + ')'
        
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
    
    def __str__(self):
        return self.content
    
