from django.shortcuts import render, redirect
from .models import Trainee


def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, "trainee/trainee_list.html", {"trainees": trainees})


def add_trainee(request):
    if request.method == "POST":
        name = request.POST["name"]
        Trainee.objects.create(name=name)
        return redirect("trainee_list")
    return render(request, "trainee/add_trainee.html")


def update_trainee(request, id):
    trainee = Trainee.objects.get(id=id)
    if request.method == "POST":
        trainee.name = request.POST["name"]
        trainee.save()
        return redirect("trainee_list")
    return render(request, "trainee/update_trainee.html", {"trainee": trainee})


def delete_trainee(request, id):
    Trainee.objects.get(id=id).delete()
    return redirect("trainee_list")
