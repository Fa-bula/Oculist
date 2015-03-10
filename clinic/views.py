from django.shortcuts import render, get_object_or_404
from clinic.models import Doctor, Service, Comment

def doctors_list(request):
    doctors_list = Doctor.objects.order_by('-birthDate')[:5]
    context = {'doctors_list': doctors_list}
    return render(request, 'clinic/doctors_list.html', context)

def services_list(request):
    services_list = Service.objects.order_by('cost')[:5]
    context = {'services_list': services_list}
    return render(request, 'clinic/services_list.html', context)

def doctor_page(request, doctor_id):
    context = {'doctor':  get_object_or_404(Doctor, pk=doctor_id)}
    return render(request, 'clinic/doctor.html', context)

def service_page(request, service_id):
    context = {'service':  get_object_or_404(Service, pk=service_id), 'comments': Comment.objects.order_by('-pubDate')}
    return render(request, 'clinic/service.html', context)

def index(request):
    return render(request, 'clinic/index.html')

def leave_comment(request, service_id):
    content = request.POST['content']
    comment = Comment(content=content, service=get_object_or_404(Service, pk=service_id))
    comment.save()
    # FIXME: Duplicate code
    context = {'service':  get_object_or_404(Service, pk=service_id), 'comments': Comment.objects.order_by('-pubDate')}
    return render(request, 'clinic/service.html', context)

    
