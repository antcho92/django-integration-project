from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

class CourseManager(models.Manager):
    def add_course(self, form_data):
        print("validating new course")
        errors = []
        # Check for empty course name
        if len(form_data['name']) == 0:
            errors.append("Invalid Course Name")
        courses = Course.objects.filter(name=form_data['name'])
        if courses:
            errors.append("Course has already been added to database")

        if len(errors) is not 0:
            print("Failed course validations")
            return (False, errors)
        else:
            print("Passed validations. Adding course to database")
            course = Course.objects.create(name=form_data['name'], description=form_data['description'])
            return (True, course)

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
