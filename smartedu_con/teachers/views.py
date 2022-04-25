from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView
from django.views.generic import DetailView


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    ordering = ['name']
    queryset = Teacher.objects.all()
    paginate_by = 1


class TeacherDetail(DetailView):
    model = Teacher
    template_name = 'teacher.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = Teacher.objects.get(pk=self.kwargs['pk'])
        context['courses'] = context['teacher'].courses.all()
        return context
