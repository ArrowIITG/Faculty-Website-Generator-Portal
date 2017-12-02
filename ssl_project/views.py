from django.shortcuts import render
from django.views.generic import DetailView , ListView,TemplateView
from userprofile.models import About_us , Teaching , Students , Projects , Publications , Recognitions,Mail,Notification,NewsFeed
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import operator
from django.db.models import Q
import functools
import ssl
user = get_user_model()
import re
from datetime import *



@login_required(login_url="/accounts/login/")
def test_view(request , slug ):
    try:
        about_us = About_us.objects.get(username__username = slug)
         #python script to fetch notifications
        mail_info = Mail.objects.get(webmail = request.user)
        pattern1 = re.compile("congrat*...*promoted")
        pattern2 = re.compile("research paper*...*accepted")
        pattern22 = re.compile("research paper*...*approved")
        pattern3 = re.compile("..*start*...*new*...*project")
        pattern4 = re.compile("...*course*...")
#promotion
        if re.search(pattern1,mail_info.mail_info) :
            print("yes")
            if Notification.objects.filter(notify_type__iexact="promotion",webmail=request.user).count()==0:
                print("yes")
                n = Notification(webmail = request.user)
                n.notify_type = "promotion"
                n.description = "Congratulations on your promotion"
                n.flag = False
                n.save()
                m = NewsFeed(webmail=request.user)
                m.first_name=User.objects.get(username=request.user).first_name
                m.last_name=User.objects.get(username=request.user).last_name
                m.description="has been promoted"
                m.created = datetime.now()
                m.save()
#research paper1
        if re.search(pattern2,mail_info.mail_info) :
            print("yes")
            if Notification.objects.filter(notify_type__iexact="publication",webmail=request.user).count()==0:
                print("yes")
                n = Notification(webmail = request.user)
                n.notify_type = "publication"
                n.description = "New Research Paper Accepted"
                n.flag = False
                n.save()
                m = NewsFeed(webmail=request.user)
                m.first_name=User.objects.get(username=request.user).first_name
                m.last_name=User.objects.get(username=request.user).last_name
                m.description="new research paper accepted"
                m.created = datetime.now()
                m.save()
#research paper2
        elif re.search(pattern22,mail_info.mail_info) :
            print("yes")
            if Notification.objects.filter(notify_type__iexact="publication",webmail=request.user).count()==0:
                print("yes")
                n = Notification(webmail = request.user)
                n.notify_type = "publication"
                n.description = "New Research Paper Accepted"
                n.flag = False
                n.save()
                m = NewsFeed(webmail=request.user)
                m.first_name=User.objects.get(username=request.user).first_name
                m.last_name=User.objects.get(username=request.user).last_name
                m.description="new research paper accepted"
                m.created = datetime.now()
                m.save()
#project
        if re.search(pattern3,mail_info.mail_info) :
            print("yes")
            if Notification.objects.filter(notify_type__iexact="project",webmail=request.user).count()==0:

                print("yes")
                n = Notification(webmail = request.user)
                n.notify_type = "project"
                n.description = "New Project"
                n.flag = False
                n.save()
                m = NewsFeed(webmail=request.user)
                m.first_name=User.objects.get(username=request.user).first_name
                m.last_name=User.objects.get(username=request.user).last_name
                m.description="has started a new project"
                m.created = datetime.now()
                m.save()
#course
        if re.search(pattern3,mail_info.mail_info) :
            print("yes")
            if Notification.objects.filter(notify_type__iexact="course",webmail=request.user).count()==0:

                print("yes")
                n = Notification(webmail = request.user)
                n.notify_type = "course"
                n.description = "New Course"
                n.flag = False
                n.save()
                m = NewsFeed(webmail=request.user)
                m.first_name=User.objects.get(username=request.user).first_name
                m.last_name=User.objects.get(username=request.user).last_name
                m.description="will be teaching course xyz this semester"
                m.created = datetime.now()
                m.save()

        notifications = Notification.objects.all()
        ncount = Notification.objects.all().count()
        mail = Mail.objects.get(webmail=request.user)
        mail.mail_info = ''
        mail.save()
#end
        news = NewsFeed.objects.order_by('-created')
        context = {
           'about_us': about_us,
           'username_name':slug,
           'notifications':notifications,
           'ncount':ncount,
           'news' : news,
        }
        return render(request, 'test.html', context)
    except:
        return redirect('userprofile:profile_about_us')


class ThanksPage(TemplateView):
    template_name = 'index.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated():
                context  = {
                    'about_us':About_us.objects.get(username__username = request.user),
                    'username_name':request.user,
                }
                return redirect('test' , slug=request.user )

        return super().get(request, *args, **kwargs)
