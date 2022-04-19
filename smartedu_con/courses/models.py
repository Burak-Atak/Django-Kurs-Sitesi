from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Course name',
                            help_text='Type course name',
                            null=False,
                            blank=False,
                            )
    description = models.TextField(blank=True,
                                   null=True,
                                   )
    image = models.ImageField(upload_to='courses/images/%Y/%m/%d',
                              blank=False,
                              null=False
                              )  # default='courses/images/default.png'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
