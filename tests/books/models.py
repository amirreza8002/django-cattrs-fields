from django.db import models


class Book(models.Model):  # noqa: DJ008
    pdf = models.FileField(upload_to="media/", null=True)
