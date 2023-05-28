from django.contrib import admin

# Register your models here.
from django.contrib import admin
from homeapp.models import  Contact_us, Slide, Service,About_us, Our_mission, Work_skill,Logo
# Register your models here.
admin.site.register(Contact_us)
admin.site.register(Slide)
admin.site.register(Service)

admin.site.register(About_us)
admin.site.register(Our_mission)
admin.site.register(Work_skill)
admin.site.register(Logo)