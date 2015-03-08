from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def doctor_page(request, doctor_id):
    return HttpResponse("You're looking at doctor %s." % doctor_id)

def service_page(request, service_id):
    return HttpResponse("You're looking at service %s." % service_id)
