from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('job-post/', views.job_post, name='job-post'),
    path('posted-job/', views.posted_jobs, name='posted-job'),
    path('job-listing/', views.job_listing, name="job-listing"),
    path('applied-job/', views.applied_jobs, name="applied-job"),
    path('job-single/<int:id>/', views.job_single, name='job-single'),
    path('apply/<int:id>/', views.apply_job, name='apply'),
    path('delete/<int:id>/', views.delete_job, name='delete'),

]
