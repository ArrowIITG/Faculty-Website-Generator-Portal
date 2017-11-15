from django.conf.urls import url , include
from django.contrib import admin
from . import views



app_name = 'userprofile'

urlpatterns = [

    url(r'^(?P<slug>[\w.@+-]+)/list$', views.Departmentwise_list ,name='Departmentwise_list'),
#about_us
    url(r'^profile_about_us$', views.About_us_create ,name='profile_about_us_create'),
    url(r'^(?P<slug>[\w.@+-]+)/about_us_user$', views.About_us_view ,name='profile_about_us'),
    url(r'^(?P<slug>[\w.@+-]+)/about_us/edit$', views.About_us_edit ,name='profile_about_us_edit'),
    url(r'^(?P<slug>[\w.@+-]+)/about_us$', views.About_us_view_logout_user ,name='profile_about_us_logout_user'),

# teaching
    url(r'^profile_teaching$', views.Teaching_create ,name='profile_teaching_create'),
    url(r'^(?P<slug>[\w.@+-]+)/teaching_user$', views.Teaching_view ,name='profile_teaching'),
    url(r'^(?P<slug>[\w.@+-]+)/teaching/(?P<pk>[0-9]+)/edit$', views.Teaching_edit ,name='profile_teaching_edit'),
    url(r'^(?P<slug>[\w.@+-]+)/teaching/(?P<pk>[0-9]+)/delete$', views.Teaching_delete ,name='profile_teaching_delete'),
    url(r'^(?P<slug>[\w.@+-]+)/teaching$', views.Teaching_view_logout_user ,name='profile_teaching_logout_user'),



#Students
    url(r'^profile_students$', views.Students_create ,name='profile_students_create'),
    url(r'^(?P<slug>[\w.@+-]+)/students_user$', views.Students_view ,name='profile_students'),
    url(r'^(?P<slug>[\w.@+-]+)/students$', views.Students_view_logout_user ,name='profile_students_logout_user'),
    url(r'^(?P<slug>[\w.@+-]+)/students/(?P<pk>[0-9]+)/edit$', views.Students_edit ,name='profile_students_edit'),
    url(r'^(?P<slug>[\w.@+-]+)/students/(?P<pk>[0-9]+)/delete$', views.Students_delete ,name='profile_students_delete'),

#projects
    url(r'^profile_projects$', views.Projects_create ,name='profile_projects_create'),
    url(r'^(?P<slug>[\w.@+-]+)/projects_user$', views.Projects_view ,name='profile_projects'),
    url(r'^(?P<slug>[\w.@+-]+)/projects$', views.Projects_view_logout_user ,name='profile_projects_logout_user'),
    url(r'^(?P<slug>[\w.@+-]+)/projects/(?P<pk>[0-9]+)/edit$', views.Projects_edit ,name='profile_projects_edit'),
    url(r'^(?P<slug>[\w.@+-]+)/projects/(?P<pk>[0-9]+)/delete$', views.Projects_delete ,name='profile_projects_delete'),

#publications
    url(r'^profile_publications$', views.Publications_create ,name='profile_publications_create'),
    url(r'^(?P<slug>[\w.@+-]+)/publications_user$', views.Publications_view ,name='profile_publications'),
    url(r'^(?P<slug>[\w.@+-]+)/publications$', views.Publications_view_logout_user ,name='profile_publications_logout_user'),
    url(r'^(?P<slug>[\w.@+-]+)/publications/(?P<pk>[0-9]+)/edit$', views.Publications_edit ,name='profile_publications_edit'),

# Recognitions
    url(r'^profile_recognitions$', views.Recognitions_create ,name='profile_recognitions_create'),
    url(r'^(?P<slug>[\w.@+-]+)/recognitions_user$', views.Recognitions_view ,name='profile_recognitions'),
    url(r'^(?P<slug>[\w.@+-]+)/recognitions$', views.Recognitions_view_logout_user ,name='profile_recognitions_logout_user'),

]
