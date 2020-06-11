from django.contrib import admin
from .models import Candidate, CandidateHardSkill, CandidateSoftSkill, Company, Location

# Company
class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields     = {'slug': ('title',)}
    search_fields           = ('title',)

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