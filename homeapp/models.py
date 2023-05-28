from django.db import models

# Create your models here.
class Contact_us(models.Model):

    sender_name=models.CharField(max_length=100)
    from_email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_email
    
    
class Slide(models.Model):

    image = models.ImageField(upload_to='slides/')

    def __str__(self):
        return "image-slide"
    
class Logo(models.Model):

    image = models.ImageField(upload_to='logo/')
    title=models.CharField(max_length=30)
    def __str__(self):
            return self.title
    
class Service(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class About_us(models.Model):
       description=models.TextField()
       
       def __str__(self):
        return "about"
    
class Our_mission(models.Model):
       description=models.TextField()
       
       def __str__(self):
        return "mission"
    
class Work_skill(models.Model):
       description=models.TextField()
       
       def __str__(self):
        return "workSkill"