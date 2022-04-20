from django.urls import path
from . import views

urlpatterns = [
    path("", views.TeacherListView.as_view(), name="teachers"),
    path("<int:teacher_id>", views.teacher_detail, name="teacher_detail"),
]
