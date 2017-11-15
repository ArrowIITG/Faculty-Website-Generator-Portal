from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User




class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated():
                context={
                    'user':request.user
                }
                return render(request , "test.html" , context)
        return super().get(request, *args, **kwargs)
