from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=25)
    course_id= models.IntegerField(primary_key=True, default=0)

    def __str__(self):
        return self.name
