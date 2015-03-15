from django.shortcuts import render, get_object_or_404
from clinic.models import Doctor, Service, Comment, Visit
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
import datetime

def doctors_list(request):
    doctors_list = Doctor.objects.order_by('-birthDate')[:5]
    context = {'doctors_list': doctors_list}
    return render(request, 'clinic/doctors_list.html', context)

def services_list(request):
    services_list = Service.objects.order_by('cost')[:5]
    context = {'services_list': services_list}
    return render(request, 'clinic/services_list.html', context)

def doctor_page(request, doctor_id):
    # FIXME: Как-то по-другому доставать service
    context = {'doctor':  get_object_or_404(Doctor, pk=doctor_id), 
               'service': Service.objects.filter(serviceType=Service.VIS).filter(doctor_id = doctor_id)[0]}
    return render(request, 'clinic/doctor.html', context)

def service_page(request, service_id):
    context = {'service':  get_object_or_404(Service, pk=service_id), 
               'comments': Comment.objects.filter(service_id=service_id)}
    return render(request, 'clinic/service.html', context)

def index(request):
    return render(request, 'clinic/index.html')

def leave_comment(request, service_id):
    content = request.POST['content']
    comment = Comment(content=content, service=get_object_or_404(Service, pk=service_id))
    comment.save()
    # return HttpResponseRedirect('clinic/services/' + str(service_id))
    # FIXME: Duplicate code
    context = {'service':  get_object_or_404(Service, pk=service_id), 'comments': Comment.objects.order_by('-pubDate')}
    return render(request, 'clinic/service.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
        return render(request, 'clinic/index.html')
    else:
        form = UserCreationForm()
        return render(request, "clinic/register.html", {
            'form': form,
        })

@login_required(login_url='/login')
def make_appointment(request, service_id):
    if request.method == 'POST':
        date_time = datetime.datetime.strptime(request.POST['dateTime'], "%d/%m/%Y %H:%M")
        visit = Visit(patient=request.user.patient, dateTime=date_time.strftime("%Y-%m-%d %H:%M"))
        visit.save()
        return render(request, 'clinic/index.html', {
            'message': date_time.strftime("%Y-%m-%d %H:%M")})
    else:
        service = get_object_or_404(Service, pk=service_id)
        context = {'service':  service,
            'minDate': '03/03/2015',
            'maxDate': '23/03/2015',
            'startWeek': service.doctor.schedule.weekdayFrom,
            'endWeek': service.doctor.schedule.weekdayTo,
            'startDay': service.doctor.schedule.hourFrom.strftime("%H:%M"),
            'endDay': service.doctor.schedule.hourTo.strftime("%H:%M"),
            'allowTimes': [
                '15:30',
                '11:00',
                '15:00',
                '27:00'],
            'weekends': ['10/03/2015']
            }
        return render(request, 'clinic/appointment.html', context)
    
