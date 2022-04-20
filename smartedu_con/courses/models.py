from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Course name',
                            help_text='Type course name',
                            null=False,
                            blank=False,
                            )
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    description = models.TextField(blank=True,
                                   null=True,
                                   )
    image = models.ImageField(upload_to='courses/%Y/%m/%d',
                              blank=False,
                              null=False,
                              default='courses/defaultImage2.png'
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
##
