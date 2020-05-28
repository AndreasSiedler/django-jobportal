from django.contrib import admin
from .models import *
from django.template.defaultfilters import slugify

# Type
class TypeHardSkillInline(admin.TabularInline):
    model                   = TypeHardSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class TypeSoftSkillInline(admin.TabularInline):
    model                   = TypeSoftSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class TypeAdmin(admin.ModelAdmin):
    inlines                 = (TypeSoftSkillInline, TypeHardSkillInline,)
    # prepopulated_fields     = {'slug': ('title', 'level')}
    filter_horizontal       = ('offers', 'tasks',)
    search_fields           = ('title',)
    readonly_fields         = ('slug',)

    def save_model(self, request, obj, form, change):
        index_skill_level   = int(form.cleaned_data['level']) - 1
        skill_level         = TYPE_LEVEL[index_skill_level][1]
        obj.slug            = f"{slugify(form.cleaned_data['title'])}-{slugify(skill_level)}"
        obj.save()


# Jobs
class JobHardSkillInline(admin.TabularInline):
    model                   = JobHardSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class JobSoftSkillInline(admin.TabularInline):
    model                   = JobSoftSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class JobAdmin(admin.ModelAdmin):
    inlines                 = (JobHardSkillInline, JobSoftSkillInline,)
    # fields                  = ('title', 'description', 'location', 'tasks', 'offers', 'company',)
    autocomplete_fields     = ['type', 'location',]
    filter_horizontal       = ('offers', 'tasks',)
    readonly_fields     = ('id',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

# Title
class TitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields       = ('title',)

# Offer
class OfferAdmin(admin.ModelAdmin):
    search_fields       = ('title',)
    readonly_fields     = ('id',)


# Task
class TaskAdmin(admin.ModelAdmin):
    search_fields       = ('title',)
    readonly_fields     = ('id',)


# Skill
class SoftskillAdmin(admin.ModelAdmin):
    search_fields       = ('name',)
    readonly_fields     = ('id',)


class HardskillAdmin(admin.ModelAdmin):
    search_fields       = ('title',)
    readonly_fields     = ('id',)


# Location
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields       = ('title',)
    readonly_fields     = ('id',)


# Category
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields     = ('id',)



# Register your models here.
admin.site.register(Type, TypeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Softskill, SoftskillAdmin)
admin.site.register(Hardskill, HardskillAdmin)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Location, LocationAdmin) 
