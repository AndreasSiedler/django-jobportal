from django.contrib import admin
from .models import Job, Type, Skill, Location, Category  

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Job)
admin.site.register(Type)
admin.site.register(Skill)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Location, LocationAdmin) 
