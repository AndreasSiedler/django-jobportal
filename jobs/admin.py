from django.contrib import admin
from .models import Job, Title, Skill, Skillship, Location, Category  



class SkillshipInline(admin.TabularInline):
    model = Skillship
    extra = 1 # how many rows to show

class JobAdmin(admin.ModelAdmin):
    inlines = (SkillshipInline,)
    list_filter = ('title__title', 'title',)
    search_fields = ('title__title', 'title',)
    fields = ('title', 'location', 'tasks', 'offers', 'company',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

class TitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Skill)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Location, LocationAdmin) 
