from django import forms
from .models import Trainee
from course_app.models import Course
from mentor_app.models import Mentor


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ["name", "course", "mentor"]

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), empty_label="Select a Course"
    )

    mentor = forms.ModelChoiceField(
        queryset=Mentor.objects.all(), empty_label="Select a Mentor", required=False
    )
