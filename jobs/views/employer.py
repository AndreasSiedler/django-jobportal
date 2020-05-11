from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template import loader


from jobs.decorators import user_is_employer
from jobs.forms import CreateJobForm, AddSkillForm
from jobs.models import Job, Applicant


class SkillAddView(UpdateView):
    template_name = 'jobs/add_skill.html'
    form_class = AddSkillForm
    extra_context = {
        'title': 'Add Skill'
    }
    success_url = reverse_lazy('jobs:employer-dashboard')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Job, id=id_)



class DashboardView(ListView):
    model = Job
    template_name = 'dash/index.html'
    context_object_name = 'jobs'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)


class ApplicantPerJobView(ListView):
    model = Applicant
    template_name = 'jobs/employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 1

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return Applicant.objects.filter(job_id=self.kwargs['job_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.get(id=self.kwargs['job_id'])
        return context

class JobUpdateView(UpdateView):
    template_name = 'jobs/create.html'
    form_class = CreateJobForm
    extra_context = {
        'title': 'Update Job'
    }
    success_url = reverse_lazy('jobs:employer-dashboard')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Job, id=id_)


class JobDeleteView(DeleteView):
    template_name = 'jobs/delete.html'
    form_class = CreateJobForm
    extra_context = {
        'title': 'Delete Job'
    }
    success_url = reverse_lazy('jobs:employer-dashboard')
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Job, id=id_)



class JobCreateView(CreateView):
    template_name = 'dash/pages/create.html'
    form_class = CreateJobForm
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('jobs:employer-dashboard')

    # dispatch MUST RETURN HTTPResponse OBJECT
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('accounts:login'))
        if self.request.user.is_authenticated and self.request.user.is_employee:
            return HttpResponseRedirect(reverse_lazy('accounts:login'))
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        job = form.save()
        return redirect('jobs:employer-skill-add', id=job.id)

    # dispatch MUST RETURN HTTPResponse OBJECT
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ApplicantsListView(ListView):
    model = Applicant
    template_name = 'jobs/employer/all-applicants.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        # jobs = Job.objects.filter(user_id=self.request.user.id)
        return self.model.objects.filter(job__user_id=self.request.user.id)


@login_required(login_url=reverse_lazy('accounts:login'))
def filled(request, job_id=None):
    try:
        job = Job.objects.get(user_id=request.user.id, id=job_id)
        job.filled = True
        job.save()
    except IntegrityError as e:
        print(e.message)
        return HttpResponseRedirect(reverse_lazy('jobs:employer-dashboard'))
    return HttpResponseRedirect(reverse_lazy('jobs:employer-dashboard'))
