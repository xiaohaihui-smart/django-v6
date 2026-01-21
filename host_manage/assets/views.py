from django.shortcuts import render

# Create your views here.
import subprocess
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Host


@api_view(['POST'])
def create_host(request):
    data = request.data
    host = Host.objects.create(
        hostname=data['hostname'],
        ip=data['ip'],
        idc_id=data['idc_id'],
        root_password=data['root_password']
    )
    return Response({'id': host.id})


@api_view(['GET'])
def ping_host(request, host_id):
    host = Host.objects.get(id=host_id)
    result = subprocess.call(
        ['ping', '-c', '1', host.ip],
        stdout=subprocess.DEVNULL
    )
    alive = result == 0
    if alive:
        host.last_ping_time = timezone.now()
        host.save()
    return Response({'alive': alive})
