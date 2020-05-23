from django.contrib import admin
from .models import PROFILE_LEVEL, Profile, ProfileSoftSkill, ProfileHardSkill, Job, Title, Offer, Task, Softskill, Hardskill, Skillship, Location, Category
from django.template.defaultfilters import slugify

# Profiles
class ProfileHardSkillInline(admin.TabularInline):
    model                   = ProfileHardSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class ProfileSoftSkillInline(admin.TabularInline):
    model                   = ProfileSoftSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class ProfileAdmin(admin.ModelAdmin):
    inlines                 = (ProfileSoftSkillInline, ProfileHardSkillInline,)
    # prepopulated_fields     = {'slug': ('title', 'level')}
    filter_horizontal       = ('offers', 'tasks',)

    def save_model(self, request, obj, form, change):
        # don't overwrite manually set slug
        if form.cleaned_data['slug'] == "":
            obj.slug = slugify(form.cleaned_data['title']) + "-" + slugify(form.cleaned_data['level'])
        obj.save()


# Jobs
class SkillshipInline(admin.TabularInline):
    model                   = Skillship
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class JobAdmin(admin.ModelAdmin):
    inlines                 = (SkillshipInline,)
    list_filter             = ('title__title', 'title',)
    search_fields           = ('title__title', 'title',)
    fields                  = ('title', 'description', 'location', 'tasks', 'offers', 'company',)
    autocomplete_fields     = ['title', 'location',]

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

# Task
class TaskAdmin(admin.ModelAdmin):
    search_fields       = ('title',)

# Skill
class SoftskillAdmin(admin.ModelAdmin):
    search_fields       = ('name',)

class HardskillAdmin(admin.ModelAdmin):
    search_fields       = ('title',)

# Location
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields       = ('title',)

# Category
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Softskill, SoftskillAdmin)
admin.site.register(Hardskill, HardskillAdmin)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Location, LocationAdmin) 
