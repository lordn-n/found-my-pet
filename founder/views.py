import logging
from .models import Pet, Report
from django.urls import reverse
from django.http import Http404
from django.conf import settings
from django.template import loader
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render

logger = logging.getLogger(__name__)


def create_report(request):
    pet = get_object_or_404(Pet, pk=request.POST['pet'])
    information = '{name}\n\n{info}'.format(
        name=request.POST['name'],
        info=request.POST['information']
    )
    report = Report(
        pet=pet,
        location=request.POST['location'],
        information=information
    )
    report.save()
    report_url = reverse(show_report, args=[report.id])

    html_message = loader.render_to_string(
        'report.html',
        {
            'report': report,
        }
    )

    send_mail(
        f'Pet Founder :: Alguien encontro a {report.pet.name}!!!',
        f'Alguien encontro a {report.pet.name} y mando un reporte. Puedes verlo aqui: {report_url}',
        'abrunocarrillo@gmail.com',
        [report.pet.owner.email],
        fail_silently=False,
        html_message=html_message
    )

    return render(request, 'create_report.html', {'report': report})


def show_report(request, report_id):
    try:
        report = Report.objects.get(pk=report_id)
    except Pet.DoesNotExist:
        raise Http404('No se encuentra el reporte....')
    return render(request, 'report.html', {'report': report})


def scan(request, pet_id):
    try:
        pet = Pet.objects.get(pk=pet_id)
    except Pet.DoesNotExist:
        raise Http404('La mascota no existe... :(')
    return render(
        request,
        'scan.html',
        {
            'pet': pet,
            'maps_key': settings.MAPS_KEY
        }
    )
