from django.db import models

from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Languages(models.Model):
    pr_languages = models.CharField(max_length=150)

    def __str__(self):
        return self.pr_languages


class Details(models.Model):
    title = models.CharField(max_length=100)
    pr_languages = models.ForeignKey(Languages, on_delete=models.CASCADE, null=True)
    price_per_month = models.IntegerField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pr_languages) + str(self.title)

