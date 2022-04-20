from django.db import models
from courses.models import Course

class Job(models.Model):
    """
    Model for the jobs of the teachers
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.DO_NOTHING, null=True)
    courses = models.ManyToManyField(Course, blank=True)
    description = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, max_length=100)
    image = models.ImageField(upload_to='teachers/%Y/%m/%d',
                              blank=False,
                              null=False,
                              default='teachers/defaultImage3.jpg'
                              )

    def __str__(self):
        return self.name
