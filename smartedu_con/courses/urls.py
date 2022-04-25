from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="courses"),
    path("<slug:category_slug>/<int:pk>", views.CourseDetail.as_view(), name="course_detail"),
    path("categories/<slug:category_slug>", views.course_list, name="category_detail"),
    path("tags/<slug:tag_slug>", views.course_list, name="tag_detail"),
    path("search", views.search, name="search"),
]
