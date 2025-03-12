from django.shortcuts import render, redirect
from .models import Mentor
from .forms import MentorForm

def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentor/list.html', {'mentors': mentors})

def add_mentor(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mentor_list')
    else:
        form = MentorForm()
    return render(request, 'mentor/add.html', {'form': form})
