from django.contrib import admin
from .models import Job, Type, Skill, Skillship, Location, Category  

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class SkillshipInline(admin.TabularInline):
    model = Skillship
    extra = 2 # how many rows to show

class JobAdmin(admin.ModelAdmin):
    inlines = (SkillshipInline,)

# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(Type)
admin.site.register(Skill)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Location, LocationAdmin) 
