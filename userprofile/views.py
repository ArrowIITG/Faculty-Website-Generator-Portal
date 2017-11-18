from django.shortcuts import render
from django.views.generic import DetailView , ListView
from .models import About_us , Teaching , Students , Projects , Publications , Recognitions
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .forms import about_us_form , teaching_form , students_form , projects_form , publications_form , recognitions_form
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import operator
from django.db.models import Q
import functools

user = get_user_model()
# Create your views here.

def Departmentwise_list(request , slug):
        required_list = About_us.objects.filter(username__xyz__Department = slug).order_by('username__username')

        print(request.user)

        if request.user.is_authenticated():

            about_us = About_us.objects.get(username__username = request.user.username)

            if request.method == "POST":
                if request.POST['search']=='':
                    context ={
                        'Departmentwise_list':required_list,
                        'Department':slug,
                        'about_us':about_us,
                    }
                    return render(request, 'userprofile/Homepage.html', context)


                search_args = []
                for term in request.POST['search'].split():
                    for query in ('username__first_name__istartswith', 'username__last_name__istartswith'):
                        search_args.append(Q(**{query: term}))

                Required_list = required_list.filter(functools.reduce(operator.or_, search_args))

                context ={
                    'Departmentwise_list':Required_list,
                    'Department':slug,
                    'about_us':about_us,
                }
                return render(request, 'userprofile/Homepage.html', context)

            else :
                context ={
                    'Departmentwise_list':required_list,
                    'Department':slug,
                    'about_us':about_us,
                }
                return render(request, 'userprofile/Homepage.html', context)
        else:
            if request.method == "POST":
                if request.POST['search']=='':
                    context ={
                        'Departmentwise_list':required_list,
                        'Department':slug,
                    }
                    return render(request, 'userprofile/Homepage.html', context)


                search_args = []
                for term in request.POST['search'].split():
                    for query in ('username__first_name__istartswith', 'username__last_name__istartswith'):
                        search_args.append(Q(**{query: term}))

                Required_list = required_list.filter(functools.reduce(operator.or_, search_args))

                context ={
                    'Departmentwise_list':Required_list,
                    'Department':slug,
                }
                return render(request, 'userprofile/Homepage.html', context)

            else :
                context ={
                    'Departmentwise_list':required_list,
                    'Department':slug,
                }
                return render(request, 'userprofile/Homepage.html', context)




def About_us_view_logout_user(request , slug ):
    try:
        about_us = About_us.objects.get(username__username = slug)
        context = {
           'about_us': about_us,
           'username_name':slug,
        }
        return render(request, 'userprofile/detail_about_us_logout_user.html', context)
    except:
        return HttpResponse("sorry not found")

@login_required(login_url="/accounts/login/")
def About_us_view(request , slug ):
    try:
        about_us = About_us.objects.get(username__username = slug)
        context = {
           'about_us': about_us,
           'username_name':slug,
        }
        return render(request, 'userprofile/detail_about_us.html', context)
    except:
        return redirect('userprofile:profile_about_us_create')

@login_required(login_url="/accounts/login/")
def About_us_create(request):
    if request.method == "POST":
        form = about_us_form(request.POST, request.FILES)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            info.save()
            return redirect('userprofile:profile_about_us', slug=request.user.username)
    else:
        form = about_us_form()
        return render(request , 'userprofile/about_us_edit.html' , {'form':form})


@login_required(login_url="/accounts/login/")
def About_us_edit(request , slug):
    about_us = About_us.objects.get(username__username = slug)
    if request.user.username == slug:
        if request.method == "POST":
            form = about_us_form(request.POST, request.FILES, instance=about_us)
            if form.is_valid():
                form.save()
                return redirect('userprofile:profile_about_us', slug)
        else:
            form = about_us_form(instance=about_us)
            return render(request , 'userprofile/about_us_edit.html' , {'form':form})
    else:
        return HttpResponse("Error. You are not authourized ")


def Teaching_view_logout_user(request , slug ):
    Teaching_required_list = Teaching.objects.filter(username__username = slug).order_by('year')
    about_us = About_us.objects.get(username__username = slug)



    if str(request.user) == str(slug):
        context = {
            'Teaching_Object_list':Teaching_required_list,
            'about_us':about_us,
            'username':True,
            'username_name':slug,
        }
    else :
        context = {
            'Teaching_Object_list':Teaching_required_list,
            'about_us':about_us,
            'username':False,
            'username_name':slug,
        }

    return render(request, 'userprofile/detail_teaching_logout_user.html' , context)


@login_required(login_url="/accounts/login/")
def Teaching_view(request , slug ):
    Teaching_required_list = Teaching.objects.filter(username__username = slug).order_by('year')
    about_us = About_us.objects.get(username__username = slug)

    print(request.user)
    print(str(slug))


    if str(request.user) == str(slug):
        context = {
            'Teaching_Object_list':Teaching_required_list,
            'about_us':about_us,
            'username':True,
            'username_name':slug,
        }
    else :
        context = {
            'Teaching_Object_list':Teaching_required_list,
            'about_us':about_us,
            'username':False,
            'username_name':slug,
        }

    return render(request, 'userprofile/detail_teaching.html' , context)


@login_required(login_url="/accounts/login/")
def Teaching_create(request):
    if request.method == "POST":
        form = teaching_form(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            info.save()
            return redirect('userprofile:profile_teaching', slug=request.user.username)
    else:
        form =  teaching_form()
        return render(request , 'userprofile/teaching_edit.html' , {'form':form})


@login_required(login_url="/accounts/login/")
def Teaching_edit(request , slug , pk ):
    print("durgesh")

    teaching = Teaching.objects.get( username__username=slug , pk=pk)

    if request.user.username == slug:
        if request.method == "POST":
            form = teaching_form(request.POST, instance=teaching)
            if form.is_valid():
                form.save()
                return redirect('userprofile:profile_teaching', slug)
        else:
            form = teaching_form(instance=teaching)
            return render(request , 'userprofile/teaching_edit.html' , {'form':form})
    else:
        return HttpResponse("Error. You are not authourized ")

@login_required(login_url="/accounts/login/")
def Teaching_delete(request , slug , pk):
    teaching = Teaching.objects.get( username__username=slug , pk=pk)
    teaching.delete()
    return redirect('userprofile:profile_teaching', slug)



def Students_view_logout_user(request , slug ):
        Students_required_list = Students.objects.filter(username__username = slug).order_by('Student_name')
        about_us = About_us.objects.get(username__username = slug)
        mtech_cont = Students_required_list.filter(Student_category=0)
        mtech_ongo = Students_required_list.filter(Student_category=1)
        phd_cont = Students_required_list.filter(Student_category=2)
        phd_onog = Students_required_list.filter(Student_category=3)

        if str(request.user) == str(slug):
            context = {
                'Students_required_list':Students_required_list,
                'about_us':about_us,
                'username':True,
                'username_name':slug,
                'mtech_cont':mtech_cont,
                'mtech_ongo':mtech_ongo,
                'phd_cont':phd_cont,
                'phd_onog':phd_onog,
            }
        else :
            context = {
                'Students_required_list':Students_required_list,
                'about_us':about_us,
                'username':False,
                'username_name':slug,
                'mtech_cont':mtech_cont,
                'mtech_ongo':mtech_ongo,
                'phd_cont':phd_cont,
                'phd_onog':phd_onog,
            }

        return render(request, 'userprofile/detail_students_logout_user.html' , context )


@login_required(login_url="/accounts/login/")
def Students_view(request , slug ):
        Students_required_list = Students.objects.filter(username__username = slug).order_by('Student_name')
        about_us = About_us.objects.get(username__username = slug)
        mtech_cont = Students_required_list.filter(Student_category=0)
        mtech_ongo = Students_required_list.filter(Student_category=1)
        phd_cont = Students_required_list.filter(Student_category=2)
        phd_onog = Students_required_list.filter(Student_category=3)


        if str(request.user) == str(slug):
            context = {
                'Students_required_list':Students_required_list,
                'about_us':about_us,
                'username':True,
                'username_name':slug,
                'mtech_cont':mtech_cont,
                'mtech_ongo':mtech_ongo,
                'phd_cont':phd_cont,
                'phd_onog':phd_onog,
            }
        else :
            context = {
                'Students_required_list':Students_required_list,
                'about_us':about_us,
                'username':False,
                'username_name':slug,
                    'mtech_cont':mtech_cont,
                    'mtech_ongo':mtech_ongo,
                    'phd_cont':phd_cont,
                    'phd_onog':phd_onog,
            }

        return render(request, 'userprofile/detail_students.html' , context )

@login_required(login_url="/accounts/login/")
def Students_create(request):
    if request.method == "POST":
        form = students_form(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            print(info.Student_category);
            info.save()
            return redirect('userprofile:profile_students', slug=request.user.username)
    else:
        form = students_form()
        return render(request , 'userprofile/students_edit.html' , {'form':form})


@login_required(login_url="/accounts/login/")
def Students_edit(request , slug , pk):
    students = Students.objects.get(username__username = slug, pk=pk)
    if request.user.username == slug:
        if request.method == "POST":
            form = students_form(request.POST, instance=students)
            if form.is_valid():
                form.save()

                return redirect('userprofile:profile_students', slug)
        else:
            form = students_form(instance=students)
            return render(request , 'userprofile/students_edit.html' , {'form':form})
    else:
        return HttpResponse("Error. You are not authourized ")

@login_required(login_url="/accounts/login/")
def Students_delete(request , slug , pk):
    students = Students.objects.get( username__username=slug , pk=pk)
    students.delete()
    return redirect('userprofile:profile_students', slug)


def Projects_view_logout_user(request , slug ):
    projects_required_list = Projects.objects.filter(username__username = slug).order_by('Start_year')
    about_us = About_us.objects.get(username__username = slug)

    context = {
        'Projects_required_list':projects_required_list,
        'username_name':slug,
        'about_us':about_us,
    }
    return render(request, 'userprofile/detail_projects_logout_user.html' , context)

@login_required(login_url="/accounts/login/")
def Projects_view(request , slug ):
    projects_required_list = Projects.objects.filter(username__username = slug).order_by('Start_year')
    about_us = About_us.objects.get(username__username = slug)
    context = {
        'Projects_required_list':projects_required_list,
        'about_us':about_us,
        'username_name':slug,
    }
    return render(request, 'userprofile/detail_projects.html' , context)


@login_required(login_url="/accounts/login/")
def Projects_create(request):
    if request.method == "POST":
        form = projects_form(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            info.save()
            return redirect('userprofile:profile_projects', slug=request.user.username)
    else:
        form = projects_form()
        context = {
            'form':form,
        }
        return render(request , 'userprofile/projects_edit.html' , context )


@login_required(login_url="/accounts/login/")
def Projects_edit(request , slug , pk ):
    projects = Projects.objects.get(username__username = slug , pk=pk)
    if request.user.username == slug:
        if request.method == "POST":
            form = projects_form(request.POST, instance=projects)
            if form.is_valid():
                form.save()
                return redirect('userprofile:profile_projects', slug)
        else:
            form = projects_form(instance=projects)
            return render(request , 'userprofile/projects_edit.html' , {'form':form})
    else:
        return HttpResponse("Error. You are not authourized ")

@login_required(login_url="/accounts/login/")
def Projects_delete(request , slug , pk):
    projects = Projects.objects.get( username__username=slug , pk=pk)
    projects.delete()
    return redirect('userprofile:profile_projects', slug)


def Publications_view_logout_user(request , slug ):
    publications_required_list = Publications.objects.filter(username__username = slug)
    about_us = About_us.objects.get(username__username = slug)
    pub_pub = publications_required_list.filter(Type=0)
    pub_books = publications_required_list.filter(Type=1)


    context = {
        'Publications_required_list':publications_required_list,
        'username_name':slug,
        'about_us':about_us,
        'pub_pub':pub_pub,
        'pub_books':pub_books,
    }
    return render(request, 'userprofile/detail_publications_logout_user.html' , context)

@login_required(login_url="/accounts/login/")
def Publications_view(request , slug ):
    publications_required_list = Publications.objects.filter(username__username = slug)
    about_us = About_us.objects.get(username__username = slug)
    pub_pub = publications_required_list.filter(Type=0)
    pub_books = publications_required_list.filter(Type=1)


    context = {
        'Publications_required_list':publications_required_list,
        'username_name':slug,
        'about_us':about_us,
        'pub_pub':pub_pub,
        'pub_books':pub_books,
    }
    return render(request, 'userprofile/detail_publications.html' , context)


@login_required(login_url="/accounts/login/")
def Publications_edit(request , slug , pk ):
    publications = Publications.objects.get(username__username = slug , pk=pk)
    if request.user.username == slug:
        if request.method == "POST":
            form = publications_form(request.POST, instance=publications)
            if form.is_valid():
                form.save()
                return redirect('userprofile:profile_publications', slug)
        else:
            form = publications_form(instance=publications)
            return render(request , 'userprofile/publications_edit.html' , {'form':form})
    else:
        return HttpResponse("Error. You are not authourized ")




@login_required(login_url="/accounts/login/")
def Publications_create(request):
    if request.method == "POST":
        form = publications_form(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            info.save()
            return redirect('userprofile:profile_publications', slug=request.user.username)
    else:
        form = publications_form()
        return render(request , 'userprofile/publications_edit.html' , {'form':form})


def Recognitions_view_logout_user(request , slug ):
    recognitions_required_list = Recognitions.objects.filter(username__username = slug)
    about_us = About_us.objects.get(username__username = slug)

    context = {
        'Recognitions_required_list':recognitions_required_list,
        'username_name':slug,
        'about_us':about_us,
    }
    return render(request, 'userprofile/detail_recognitions_logout_user.html' , context)


@login_required(login_url="/accounts/login/")
def Recognitions_view(request , slug ):
    recognitions_required_list = Recognitions.objects.filter(username__username = slug)
    about_us = About_us.objects.get(username__username = slug)


    context = {
        'Recognitions_required_list':recognitions_required_list,
        'about_us':about_us,
        'username_name':slug,
    }
    return render(request, 'userprofile/detail_recognitions.html' , context)


@login_required(login_url="/accounts/login/")
def Recognitions_create(request):
    if request.method == "POST":
        form = recognitions_form(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.username = request.user
            info.save()
            return redirect('userprofile:profile_recognitions', slug=request.user.username)
    else:
        form = recognitions_form()
        return render(request , 'userprofile/recognitions_edit.html' , {'form':form})
