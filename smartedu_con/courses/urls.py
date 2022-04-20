from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="courses"),
    path("<slug:category_slug>/<int:course_id>", views.course_detail, name="course_detail"),
    path("categories/<slug:category_slug>", views.category_detail, name="category_detail"),
    path("tags/<slug:tag_slug>", views.tag_detail, name="tag_detail"),
]
