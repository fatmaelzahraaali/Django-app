from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=25)
    id= models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
