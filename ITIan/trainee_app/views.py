from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm
from course_app.models import Course
from mentor.models import Mentor

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, "trainee/trainee_list.html", {"trainees": trainees})


def add_trainee(request):
    if request.method == "POST":
        form = TraineeForm(request.POST)
        if form.is_valid():
            trainee = form.save(commit=False)  
            trainee.course = Course.objects.get(id=request.POST["course"])  
            trainee.mentor = Mentor.objects.get(id=request.POST["mentor"])  
            trainee.save()
            return redirect('trainee_list')  
    else:
        form = TraineeForm()

    return render(request, 'trainee/add_trainee.html', {'form': form})


def update_trainee(request, id):
    trainee = Trainee.objects.get(id=id)
    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)
    
    return render(request, 'trainee/update_trainee.html', {'form': form})



def delete_trainee(request, id):
    Trainee.objects.get(id=id).delete()
    return redirect("trainee_list")
