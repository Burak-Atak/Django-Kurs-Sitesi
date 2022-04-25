from django.shortcuts import render
from .models import Course, Tag, Category
from django.views.generic import DetailView
from django.db.models import Q


def course_list(request, category_slug=None, tag_slug=None):
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')

    if category_slug is not None:
        courses = Course.objects.all().filter(category__slug=category_slug).order_by('-created_at')
    elif tag_slug is not None:
        courses = Course.objects.all().filter(tags__slug=tag_slug).order_by('-created_at')
    else:
        courses = Course.objects.all().order_by('-created_at')
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories
    }

    return render(request, 'courses.html', context)


class CourseDetail(DetailView):
    model = Course
    template_name = 'course.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs['pk'])
        context['teachers'] = context['course'].teacher_set.all()
        return context


def search(request):
    query = request.GET.get('search')
    courses = Course.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    context = {
        'courses': courses,
        'tags': tags,
        'categories': categories
    }
    return render(request, 'courses.html', context)
