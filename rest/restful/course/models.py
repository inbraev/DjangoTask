from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    imgpath = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Branch(models.Model):
    longitude = models.CharField(max_length=100, blank=True, default='')
    latitude = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    PHONE = 1
    FACEBOOK = 2
    EMAIL = 3

    item = [
        (PHONE, "Phone"),
        (FACEBOOK, "Facebook"),
        (EMAIL, "Email"),
    ]
    type = models.IntegerField(choices=item, default='PHONE')
    value=models.CharField(max_length=100, blank=True, default='')
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    logo = models.CharField(max_length=300, blank=True, default='')
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
