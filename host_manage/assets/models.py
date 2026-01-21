from django.db import models

class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class IDC(models.Model):
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE)
    root_password = models.CharField(max_length=128)
    last_ping_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.hostname


class PasswordHistory(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    old_password = models.CharField(max_length=128)
    new_password = models.CharField(max_length=128)
    changed_at = models.DateTimeField(auto_now_add=True)


class HostStatistics(models.Model):
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    idc = models.ForeignKey(IDC, on_delete=models.CASCADE)
    host_count = models.IntegerField()
