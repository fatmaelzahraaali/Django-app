from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm


def course_list(request):
    """Display all courses in a table."""
    courses = Course.objects.all()
    return render(request, "course/course_list.html", {"courses": courses})


def add_course(request):
    """Handle adding a new course using a form."""
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")  # Redirect to course list after adding
    else:
        form = CourseForm()
    return render(request, "course/add_course.html", {"form": form})


def update_course(request, course_id):
    """Handle updating an existing course."""
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")  # Redirect after update
    else:
        form = CourseForm(instance=course)
    return render(request, "course/update_course.html", {"form": form})


def delete_course(request, id):
    Course.objects.get(id=id).delete()
    return redirect("course_list")
