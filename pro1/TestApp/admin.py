from django.contrib import admin
from TestApp.models import P

# Register your models here.
class Padmin(admin.ModelAdmin):
    list_display=['fname','lname','phoneno','age','J_date','symptoms','prescription']

admin.site.register(P,Padmin)