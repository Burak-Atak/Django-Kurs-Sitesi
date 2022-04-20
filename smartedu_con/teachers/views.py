from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    ordering = ['name']
    queryset = Teacher.objects.all()
    paginate_by = 1


def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    courses = teacher.courses.all()

    context = {
        'teacher': teacher,
        'courses': courses
    }
    return render(request, 'teacher.html', context)
