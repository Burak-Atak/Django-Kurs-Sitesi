from django.urls import path
from . import views

urlpatterns = [
    path("", views.TeacherListView.as_view(), name="teachers"),
    path("<int:pk>", views.TeacherDetail.as_view(), name="teacher_detail"),
]
