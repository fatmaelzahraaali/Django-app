from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
class Trainee(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="trainees") 
    mentor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="mentees")  
    def __str__(self):
        return self.name
