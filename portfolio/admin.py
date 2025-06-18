from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Tupla para crear y actualizar 


admin.site.register(Project, ProjectAdmin)