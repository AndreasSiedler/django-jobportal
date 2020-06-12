from django.contrib import admin
from .models import *
from django.template.defaultfilters import slugify

# Language
class LanguageAdmin(admin.ModelAdmin):
    search_fields           = ('title',)


# Education
class EducationAdmin(admin.ModelAdmin):
    search_fields           = ('title',)

# Type
class TypeExperienceInline(admin.TabularInline):
    model                   = TypeExperience
    fk_name                 = "to_type"
    extra                   = 1


class TypeHardSkillInline(admin.TabularInline):
    model                   = TypeHardSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']


class TypeSoftSkillInline(admin.TabularInline):
    model                   = TypeSoftSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']

class TypeLanguageInline(admin.TabularInline):
    model                   = TypeLanguage
    extra                   = 1
    autocomplete_fields     = ['language']


class TypeAdmin(admin.ModelAdmin):
    inlines                 = (TypeExperienceInline, TypeSoftSkillInline, TypeHardSkillInline, TypeLanguageInline,)
    # prepopulated_fields     = {'slug': ('title', 'level')}
    fields                  = ('active', 'title', 'slug', 'description', 'category', 'tasks', 'offers', 'salarymin', 'salarymax', 'education', 'created_by')
    filter_horizontal       = ('offers', 'tasks',)
    autocomplete_fields     = ('education',)
    search_fields           = ('title',)
    readonly_fields         = ('slug',)
    list_display            = ('title', 'category', 'slug',)


    def save_model(self, request, obj, form, change):
        # index_skill_level   = int(form.cleaned_data['level']) - 1
        # skill_level         = TYPE_LEVEL[index_skill_level][1]
        # obj.slug            = f"{slugify(form.cleaned_data['title'])}-{slugify(skill_level)}"
        print(request.user)
        obj.slug            = f"{slugify(form.cleaned_data['title'])}"
        if getattr(obj, 'created_by', None) is None:
            obj.user = request.user
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

class JobExperienceInline(admin.TabularInline):
    model                   = JobExperience
    extra                   = 1
    autocomplete_fields     = ['type']


class JobLanguageInline(admin.TabularInline):
    model                   = JobLanguage
    extra                   = 1
    autocomplete_fields     = ['language']

class JobAdmin(admin.ModelAdmin):
    inlines                 = (JobExperienceInline, JobHardSkillInline, JobSoftSkillInline, JobLanguageInline,)
    fields                  = ('active', 'type', 'description', 'tasks', 'offers', 'salarymin', 'salarymax', 'education', 'company', 'location',)
    autocomplete_fields     = ['type', 'education', 'company', 'location',]
    # filter_horizontal       = ('offers',)
    readonly_fields         = ('id',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


# Offer
class OfferAdmin(admin.ModelAdmin):
    search_fields       = ('title',)
    readonly_fields     = ('id',)


# Task
class TaskAdmin(admin.ModelAdmin):
    search_fields       = ('title',)
    readonly_fields     = ('id',)
    list_display        = ('title', 'category',)
    list_filter         = ('title', 'category',)


# Skill
class SoftskillAdmin(admin.ModelAdmin):
    search_fields       = ('name',)
    readonly_fields     = ('id',)


class HardskillAdmin(admin.ModelAdmin):
    search_fields       = ('title',)
    readonly_fields     = ('id',)
    autocomplete_fields = ('dependency',)
    list_display        = ('title', 'dependency',)



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
admin.site.register(Education, EducationAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Softskill, SoftskillAdmin)
admin.site.register(Hardskill, HardskillAdmin)
admin.site.register(Category, CategoryAdmin) 
# admin.site.register(Location, LocationAdmin) 
