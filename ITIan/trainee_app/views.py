from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm
from course_app.models import Course
from mentor_app.models import Mentor
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("trainee_list")  # Redirect to trainee list
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "auth/login.html"


def logout_view(request):
    logout(request)
    return redirect("auth/login")


class TraineeListView(ListView):
    model = Trainee
    template_name = "trainee/trainee_list.html"  # Customize the template
    context_object_name = "trainees"


class TraineeDetailView(DetailView):
    model = Trainee
    template_name = "trainee/trainee_detail.html"
    context_object_name = "trainee"


class TraineeDeleteView(DeleteView):
    model = Trainee
    success_url = reverse_lazy("trainee_list")


class TraineeUpdateView(UpdateView):
    model = Trainee
    form_class = TraineeForm
    template_name = "trainee/update_trainee.html"
    success_url = reverse_lazy("trainee_list")


class TraineeCreateView(CreateView):
    model = Trainee
    form_class = TraineeForm
    template_name = "trainee/trainee_form.html"
    success_url = reverse_lazy("trainee_list")


# def trainee_list(request):
#     trainees = Trainee.objects.all()
#     return render(request, "trainee/trainee_list.html", {"trainees": trainees})

# def add_trainee(request):
#     if request.method == "POST":
#         form = TraineeForm(request.POST)
#         if form.is_valid():
#             trainee = form.save(commit=False)
#             trainee.course = Course.objects.get(id=request.POST["course"])
#             trainee.mentor = Mentor.objects.get(id=request.POST["mentor"])
#             trainee.save()
#             return redirect("trainee_list")
#     else:
#         form = TraineeForm()

#     return render(request, "trainee/add_trainee.html", {"form": form})


# def update_trainee(request, id):
#     trainee = Trainee.objects.get(id=id)
#     if request.method == "POST":
#         form = TraineeForm(request.POST, instance=trainee)
#         if form.is_valid():
#             form.save()
#             return redirect("trainee_list")
#     else:
#         form = TraineeForm(instance=trainee)

#     return render(request, "trainee/update_trainee.html", {"form": form})


# def delete_trainee(request, id):
#     Trainee.objects.get(id=id).delete()
#     return redirect("trainee_list")
