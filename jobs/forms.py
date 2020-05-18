from django import forms
from dal import autocomplete

from jobs.models import Job, Skill, Applicant

# class AddSkillForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = ['skills']

#     def __init__ (self, *args, **kwargs):
#         super(AddSkillForm, self).__init__(*args, **kwargs)
#         self.fields["skills"].widget = forms.widgets.CheckboxSelectMultiple()
#         self.fields["skills"].help_text = ""
#         self.fields["skills"].queryset = Skill.objects.all()


class CreateJobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateJobForm, self).__init__(*args, **kwargs)
        self.fields['location'].empty_label = "Select a Location"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Job
        exclude = ('user', 'created_at',)
        labels = {
            "last_date": "Last Date",
            "company_name": "Company Name",
            "company_description": "Company Description"
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter Description'}),
        }

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)
