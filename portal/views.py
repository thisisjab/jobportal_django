from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from . import models


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'portal/profile.html'


class JobCandidateProfileCreateView(LoginRequiredMixin, FormView):
    form_class = forms.JobCandidateProfileForm
    success_url = reverse_lazy('portal:profile')
    template_name = 'portal/jobcandidate_profile_form.html'

    def form_valid(self, form):
        models.JobCandidate(
            birth_date=form.cleaned_data['birth_date'].isoformat() if form.cleaned_data.get('birth_date', None) else None,
            short_bio=form.cleaned_data['short_bio'],
            description=form.cleaned_data['description'],
            user=self.request.user
        ).save()
        return super(JobCandidateProfileCreateView, self).form_valid(form)


class JobCandidateProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = forms.JobCandidateProfileForm
    model = models.JobCandidate
    success_url = reverse_lazy('portal:profile')
    template_name = 'portal/jobcandidate_profile_form.html'


class EmployerProfileCreateView(LoginRequiredMixin, FormView):
    form_class = forms.EmployerProfileForm
    model = models.Employer
    success_url = reverse_lazy('portal:profile')
    template_name = 'portal/employer_profile_form.html'

    def form_valid(self, form):
        models.Employer(
            short_bio=form.cleaned_data['short_bio'],
            user=self.request.user
        ).save()
        return super().form_valid(form)


class EmployerProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = forms.EmployerProfileForm
    model = models.Employer
    success_url = reverse_lazy('portal:profile')
    template_name = 'portal/employer_profile_form.html'
