from django.contrib import admin
from .models import Candidate, Company

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Company, CompanyAdmin)