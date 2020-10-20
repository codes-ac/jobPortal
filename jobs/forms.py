from django import forms
from .models import *


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        exclude = ('user', 'image')
        labels = {
            "job_location": "Job Location",
            "published_on": "Publish Date"
        }


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        exclude = ('applied_for','company_name')
        labels = {
            "file": "CV (pdf format)",
            "name": "Full Name"

        }
