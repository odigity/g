from django.contrib.auth.models         import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db                          import models


class Advisor(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name           = models.CharField(max_length=50)
    avatar              = models.URLField(null=True)


class Investor(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name           = models.CharField(max_length=50)
    avatar              = models.URLField(null=True)


class PlanCategory(models.Model):
    label               = models.CharField(max_length=50)
    icon                = models.CharField(max_length=100)


class Plan(models.Model):
    name                = models.CharField(max_length=50)
    category            = models.ForeignKey(PlanCategory, on_delete=models.CASCADE)


class Notification(models.Model):
    body                = models.CharField(max_length=50)
    metadata            = models.JSONField(default=dict)

    icon1_content_type  = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="+")
    icon1_object_id     = models.PositiveIntegerField()
    icon1_object        = GenericForeignKey('icon1_content_type', 'icon1_object_id')

    icon2_content_type  = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="+")
    icon2_object_id     = models.PositiveIntegerField()
    icon2_object        = GenericForeignKey('icon2_content_type', 'icon2_object_id')


class NotificationBlast(models.Model):
    audience            = models.CharField(max_length=10, choices=[('INVESTORS', 'Investors'), ('ADVISORS', 'Advisors'), ('BOTH', 'Both')])
    body                = models.CharField(max_length=50)
    icon                = models.CharField(max_length=100)


