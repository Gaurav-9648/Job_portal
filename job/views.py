from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"

        except:
            error = "yes"

    d = {'error':error}
    return render(request,'admin_login.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rcount = Recruiter.objects.all().count()
    scount = StudentUser.objects.all().count()
    d ={'rcount': rcount,'scount': scount}
    return render(request,'admin_home.html',d)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request,'view_users.html',d)

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)

def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Accept')
    d = {'data': data}
    return render(request, 'recruiter_accepted.html', d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Reject')
    d = {'data': data}
    return render(request, 'recruiter_rejected.html', d)

def all_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'all_recruiter.html', d)

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    recruiter = Recruiter.objects.get(id = pid)
    if request.method=="POST":
        s = request.POST['status']
        recruiter.status=s
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
    d = {'recruiter': recruiter, 'error': error}
    return render(request, 'change_status.html', d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        # cn = request.POST['confirmpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passwordadmin.html', d)

def change_passwodrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        # cn = request.POST['confirmpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passwodrecruiter.html', d)

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        # cn = request.POST['confirmpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passworduser.html', d)


def delete_users(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = StudentUser.objects.get(id=pid)
    student.delete()
    return redirect('view_users')

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error = "yes"

        else:
            error = "yes"
    d = {'error' : error}
    return render(request , 'user_login.html',d)

def recruiter_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"

        else:
            error = "yes"

    d = {'error': error}
    return render(request,'recruiter_login.html',d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        j = request.POST['jobtitle']
        s = request.POST['sdate']
        e = request.POST['endate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        sk = request.POST['skills']
        des = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter,start_date=s,end_date=e,title=j,salary=sal,
                               image=l,description=des,experience=exp,location=loc,
                               skills=sk,creationdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'add_job.html',d)

def edit_joblist(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job= Job.objects.get(id=pid)
    if request.method == 'POST':
        j = request.POST['jobtitle']
        s = request.POST['sdate']
        e = request.POST['endate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        sk = request.POST['skills']
        des = request.POST['description']

        job.title = j
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = sk
        job.description = des
        try:
            job.save()
            error = "no"
        except:
            error = "yes"

        if s:
            try:
                job.start_date = s
                job.save()
            except:
                pass
        else:
            pass

        if e:
            try:
                job.end_date = e
                job.save()
            except:
                pass
        else:
            pass

    d = {'error': error,'job': job}
    return render(request,'edit_joblist.html',d)

def change_companylogo(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job= Job.objects.get(id=pid)
    if request.method == 'POST':
        cl = request.FILES['logo']

        job.image = cl
        try:
            job.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'job': job}
    return render(request,'change_companylogo.html',d)

def applyforjob(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1 = date.today()
    if job.end_date < date1:
        error = "close"

    elif job.start_date > date1:
        error = "notopen"

    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            Apply.objects.create(job=job,student=student,resume=r,applydate=date1.today())
            error="success"
    d = {'error': error}
    return render(request,'applyforjob.html',d)


def job_listrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job' : job}
    return render(request,'job_listrecruiter.html',d)

def job_listuser(request):
    job = Job.objects.all().order_by('-start_date')
    user = request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    li =[]
    for i in data:
        li.append(i.job.id)
    d = {'job' : job,'li': li}
    return render(request,'job_listuser.html',d)

def job_detail(request,pid):
    job = Job.objects.get(id=pid)
    d = {'job' : job}
    return render(request,'job_detail.html',d)


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        g = request.POST['gender']
        con = request.POST['contact']

        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.user.gender = g
        recruiter.user.mobile = con

        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error = "no"
        except:
            pass

    d = {'recruiter':recruiter,'error': error}
    return render(request,'recruiter_home.html',d)

def Logout(request):
    logout(request)
    return redirect('index')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        g = request.POST['gender']
        con = request.POST['contact']

        student.user.first_name = f
        student.user.last_name = l
        student.user.gender = g
        student.user.mobile = con

        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error = "no"
        except:
            pass

    d = {'student': student, 'error': error}
    return render(request,'user_home.html',d)

def latest_jobs(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job': job}
    return render(request, 'latest_jobs.html', d)

def about(request):
    return render(request,'about.html')

def user_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        g = request.POST['gender']
        e = request.POST['email']
        con = request.POST['contact']
        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            StudentUser.objects.create(user=user,mobile=con,image=i,gender=g,type="student")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'user_signup.html',d)

def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        g = request.POST['gender']
        e = request.POST['email']
        con = request.POST['contact']
        company = request.POST['cmp']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=con, image=i, gender=g, company=company, type="recruiter", status="pending")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'recruiter_signup.html', d)


def appliedcandidate(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    data = Apply.objects.all()
    d = {'data': data}
    return render(request,'appliedcandidate.html',d)
