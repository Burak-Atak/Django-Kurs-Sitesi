from django.shortcuts import render
from .models import Course, Tag, Category


def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories
    }

    return render(request, 'courses.html', context)


def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')

    context = {
        'course': course,
        'tags': tags,
        'categories': categories,
    }

    return render(request, 'course.html', context)


def category_detail(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug).order_by('-created_at')
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories,
    }

    return render(request, 'courses.html', context)


def tag_detail(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug).order_by('-created_at')
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories,
    }

    return render(request, 'courses.html', context)
