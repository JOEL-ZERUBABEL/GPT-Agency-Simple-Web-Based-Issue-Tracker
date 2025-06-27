from django.db import models


# Create your models here.
class Issues(models.Model):
    status_choices=[("To Do","To Do"),
                    ("In Progress","In Progress"),
                    ("Done","Done")]
    priority_choices=[("Low","Low"),
                      ("Medium","Medium"),
                      ("High","High")]
    
    title=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=300,null=True)
    status=models.CharField(max_length=20,choices=status_choices,default="To Do")
    priority=models.CharField(max_length=20,choices=priority_choices,default="Low")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.title

