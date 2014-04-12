from django.db import models


class Timestampable(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Permalinkable(models.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True


