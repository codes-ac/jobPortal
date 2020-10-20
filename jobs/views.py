from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import *
from .models import *

from django.views.generic import ListView


def home(request):
    # qs = JobListing.objects.all()

    # context = {
    #     'query': qs,
    # }
    return render(request, "home.html")



def job_listing(request):
    qs = JobListing.objects.all().order_by('-published_on')

    context = {
        'query': qs,
    }
    return render(request, "job_listing.html", context)


def job_post(request):
    form = JobListingForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/job-listing/')
    context = {
        'form': form,

    }
    return render(request, "job_post.html", context)


def job_single(request, id):
    job_query = get_object_or_404(JobListing, id=id)

    context = {
        'q': job_query,
    }
    return render(request, "job_single.html", context)


def apply_job(request, id):
    form = JobApplyForm(request.POST or None, request.FILES)
    job_query = get_object_or_404(JobListing, id=id)
    if form.is_valid():
        instance = form.save()
        instance.applied_for = job_query.title
        instance.company_name = job_query.company_name
        instance.save()
        return redirect('/')
    context = {
        'form': form,
        'id':id,

    }
    return render(request, "job_apply.html", context)


def applied_jobs(request):
    name = 'candidate@abc.in'
    qs = ApplyJob.objects.filter(name = name).order_by("-id")

    context = {
        'query': qs,
        'name': name,
    }
    return render(request, "applied_job.html", context)


def posted_jobs(request):
    company = 'recruiter@abc.in'
    qs = JobListing.objects.filter(company_name = company).order_by('-id')

    context = {
        'query': qs,
        'company': company,
    }
    return render(request, "posted_job.html", context)

def delete_job(request, id):
    job_to_delete = get_object_or_404(JobListing, id=id) 
    job_to_delete.delete()
    return redirect('/posted-job/')



