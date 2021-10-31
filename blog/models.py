from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content =models.TextField()
    slug =models.CharField(max_length=100)
    time =models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    Level=models.CharField(max_length=20)
    Pro=models.CharField(max_length=50)
    Content=models.TextField()
    Profile_image=models.ImageField(upload_to="media",default="")
    
    def __str__(self):
        return self.First_name
    
class Comment(models.Model):
    comment=models.TextField()
    
    def __str__(self):
        return self.comment
    
    
    
    

    
    
    