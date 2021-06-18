from django.db import models
# from .forms import AdminRegistrationForm


class Projects(models.Model):
    title = models.CharField(max_length=120)
    thumb = models.ImageField(upload_to="images/")
    desc = models.TextField(max_length=1000)
    
        
    def __str__(self):
        return self.title
    

class Department(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    
    def __str__(self):
        return self.title


class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=120)
    emp_email = models.CharField(max_length=120, unique=True)
    emp_contact = models.CharField(max_length=120, null=True, blank=True)
    emp_img = models.ImageField(upload_to="images/")
    ongoing_projects = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    emp_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    salary = models.FloatField()
    status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.emp_name
    
    
    
    
    



