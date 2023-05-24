"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admindatabase/', admin.site.urls),
    path('', index,name="index"),
    path('admin_login', admin_login,name="admin_login"),
    path('admin_home', admin_home,name="admin_home"),
    path('view_users', view_users,name="view_users"),
    path('recruiter_pending', recruiter_pending,name="recruiter_pending"),
    path('recruiter_accepted', recruiter_accepted,name="recruiter_accepted"),
    path('recruiter_rejected', recruiter_rejected,name="recruiter_rejected"),
    path('all_recruiter', all_recruiter,name="all_recruiter"),
    path('change_passwordadmin', change_passwordadmin,name="change_passwordadmin"),
    path('change_passworduser', change_passworduser,name="change_passworduser"),
    path('delete_users/<int:pid>', delete_users, name="delete_users"),
    path('change_status/<int:pid>', change_status,name="change_status"),
    path('user_login', user_login,name="user_login"),
    path('recruiter_login', recruiter_login,name="recruiter_login"),
    path('latest_jobs', latest_jobs,name="latest_jobs"),
    path('about', about,name="about"),
    path('user_signup', user_signup,name="user_signup"),
    path('user_home', user_home,name="user_home"),
    path('Logout', Logout,name="Logout"),
    path('recruiter_signup', recruiter_signup,name="recruiter_signup"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    path('change_passwodrecruiter', change_passwodrecruiter, name="change_passwodrecruiter"),
    path('add_job', add_job, name="add_job"),
    path('job_listrecruiter', job_listrecruiter, name="job_listrecruiter"),
    path('job_listuser', job_listuser, name="job_listuser"),
    path('edit_joblist/<int:pid>', edit_joblist, name="edit_joblist"),
    path('applyforjob/<int:pid>', applyforjob, name="applyforjob"),
    path('change_companylogo/<int:pid>', change_companylogo, name="change_companylogo"),
    path('job_detail/<int:pid>', job_detail, name="job_detail"),
    path('appliedcandidate', appliedcandidate, name="appliedcandidate"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
