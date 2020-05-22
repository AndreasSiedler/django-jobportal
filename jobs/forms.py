from django import forms
from jobs.models import Job, Applicant
from .widgets.widgets import DynamicArrayWidget

# class AddSkillForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = ['skills']

#     def __init__ (self, *args, **kwargs):
#         super(AddSkillForm, self).__init__(*args, **kwargs)
#         self.fields["skills"].widget = forms.widgets.CheckboxSelectMultiple()
#         self.fields["skills"].help_text = ""
#         self.fields["skills"].queryset = Skill.objects.all()


# class DynamicArrayField(forms.Field):

#     default_error_messages = {
#         'item_invalid': 'Item %(nth)s in the array did not validate: ',
#     }

#     def __init__(self, base_field, **kwargs):
#         self.get = False
#         self.attrs = False
#         self.is_hidden = False
#         self.needs_multipart_form = False
#         self.base_field = base_field
#         self.max_length = kwargs.pop('max_length', None)
#         kwargs.setdefault('widget', DynamicArrayWidget)
#         super().__init__(**kwargs)

#     def clean(self, value):
#         cleaned_data = []
#         errors = []
#         value = filter(None, value)
#         for index, item in enumerate(value):
#             try:
#                 cleaned_data.append(self.base_field.clean(item))
#             except forms.ValidationError as error:
#                 errors.append(prefix_validation_error(
#                     error, self.error_messages['item_invalid'],
#                     code='item_invalid', params={'nth': index},
#                 ))
#         if errors:
#             raise forms.ValidationError(list(chain.from_iterable(errors)))
#         if cleaned_data and self.required:
#             raise forms.ValidationError(self.error_messages['required'])
#         return cleaned_data


# class JobAdminForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         widgets = {
#         'tasks': DynamicArrayField(models.CharField(max_length=300)),
#         }
#         fields = '__all__'



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
