from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages
from homeapp.models import  Contact_us, Slide, Service, Work_skill,About_us,Our_mission,Logo
# Create your views here.
def home(request):
   slides = Slide.objects.all()
   services = Service.objects.all()
   about = About_us.objects.all()
   workskill = Work_skill.objects.all()
   mission = Our_mission.objects.all()
   logos = Logo.objects.all()
   if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject = request.POST.get('subject', )
        message= request.POST.get('message')
        admin='arhammultiservice@gmail.com'
      
        if subject and message and email:
           contact=Contact_us(sender_name=name,from_email=email,subject=subject,message=message)
           contact.save()
           send_mail(subject,message,email, [admin,email,name])
           messages.success(request,'Succesfully Send Message!')
        
         
        else:
           messages.error(request,'Make sure all fields are entered and valid!')

   return render(request,'home.html',locals())


