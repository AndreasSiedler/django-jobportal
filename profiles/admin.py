from django.contrib import admin
from .models import Candidate, CandidateHardSkill, CandidateSoftSkill, Company, Location
from django.template.defaultfilters import slugify


# Company
class CompanyAdmin(admin.ModelAdmin):
    # prepopulated_fields     = {'slug': ('title',)}
    autocomplete_fields     = ('user',)
    search_fields           = ('title',)
    readonly_fields         = ('slug', 'created_by',)
    list_display            = ('title', 'slug',)

    def save_model(self, request, obj, form, change):
        obj.slug            = f"{slugify(form.cleaned_data['title'])}"
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()

# Location
class LocationAdmin(admin.ModelAdmin):
    search_fields           = ('title',)

# Candidate
class CandidateHardSkillInline(admin.TabularInline):
    model                   = CandidateHardSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']

class CandidateSoftSkillInline(admin.TabularInline):
    model                   = CandidateSoftSkill
    extra                   = 1 # how many rows to show
    autocomplete_fields     = ['skill']

class CandidateAdmin(admin.ModelAdmin):
    inlines                 = (CandidateHardSkillInline, CandidateSoftSkillInline,)
    # fields                  = ('title', 'description', 'location', 'tasks', 'offers', 'company',)
    filter_horizontal       = ('tasks',)
    autocomplete_fields     = ['user', 'jobtype']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


# Register your models here.
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)