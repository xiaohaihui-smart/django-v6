from celery import shared_task
from django.utils import timezone
from django.db.models import Count
from .models import Host, PasswordHistory, HostStatistics
import random
import string


def gen_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


@shared_task
def rotate_root_password():
    for host in Host.objects.all():
        old = host.root_password
        new = gen_password()
        host.root_password = new
        host.save()

        PasswordHistory.objects.create(
            host=host,
            old_password=old,
            new_password=new
        )


@shared_task
def daily_statistics():
    today = timezone.now().date()
    qs = Host.objects.values(
        'idc__city_id', 'idc_id'
    ).annotate(cnt=Count('id'))

    for row in qs:
        HostStatistics.objects.create(
            date=today,
            city_id=row['idc__city_id'],
            idc_id=row['idc_id'],
            host_count=row['cnt']
        )
