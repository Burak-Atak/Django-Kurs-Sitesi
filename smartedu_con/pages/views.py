from django.views.generic import TemplateView
from django.shortcuts import render
from courses.models import Course


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True)[:2]
        context['courses_count'] = Course.objects.filter(available=True).count()
        return context


def about(request):
    return render(request, 'about.html')
