from django.db import models

class CourseManager(models.Manager):
    def validator(self, data):
        
        

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    



