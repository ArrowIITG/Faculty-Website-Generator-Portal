from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.utils import timezone
from .models import About_us , Teaching , Students , Projects , Publications , Recognitions , CATEGORY



class about_us_form(forms.ModelForm):
    Upload_Profile_Pic = forms.ImageField(label='Choose Image' , required=False)
    Department = forms.CharField(max_length=60,required=True)
    Departmental_post = forms.CharField(max_length=60 , required=True)
    Room_no = forms.CharField(max_length=10 , required=True)
    phone = forms.CharField(max_length=15 , required=True , help_text="+91 must not be added in front")
    Research_interest = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols':'10','class':'form-control'}),required=True)
    primary_Research_group = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'cols':'10','class':'form-control'}))

    class Meta:
        model = About_us
        fields = ('Upload_Profile_Pic','Department', 'Departmental_post' , 'Room_no' , 'phone' ,'Research_interest' , 'primary_Research_group')


class teaching_form(forms.ModelForm):
    SEMESTER_CHOICES = (
        ( 0 , 'Even Semester'),
        ( 1 , 'Odd Semester'),
    )
    semester = forms.TypedChoiceField(choices=SEMESTER_CHOICES, widget=forms.RadioSelect, coerce=int)
    Subject_code = forms.CharField(max_length=10 , required=True)
    Subject = forms.CharField(max_length=200 , required=True)
    Partners = forms.CharField(max_length=1000 , required=False)

    class Meta:
        model = Teaching
        fields = ('year' , 'semester' , 'Subject_code' , 'Subject' , 'Partners')


class students_form(forms.ModelForm):
    Student_name = forms.CharField(max_length=100 , required=True)
    Thesis_title = forms.CharField(max_length=3000 , required=False)
    Supervisors = forms.CharField(max_length=3000 , required=False)
    Student_category = forms.IntegerField(widget=forms.Select(choices= CATEGORY) , required=True)

    class Meta:
        model = Students
        fields = ('Student_name' ,'Student_category' , 'Thesis_title' , 'Supervisors')


class projects_form(forms.ModelForm):
    TYPE_CHOICES = (
        ( 0 , ' Consultancy Research Projects'),
        ( 1 , ' Sponsored Research Projects'),
    )
    Project_Type = forms.TypedChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect, coerce=int)
    Project_title = forms.CharField(max_length=5000 , required=True)
    PI = forms.CharField(max_length=2000 , required=True)
    co_PI = forms.CharField(max_length=2000 , required=False)
    Funding_Agency = forms.CharField(max_length=2000 , required=True)

    class Meta:
        model = Projects
        fields = ('Project_Type', 'Project_title' , 'PI' , 'co_PI' , 'Funding_Agency' , 'Start_year' , 'End_Year' )


class publications_form(forms.ModelForm):
    TYPE_CHOICES = (
        ( 0 , ' Publications'),
        ( 1 , ' Books/Book Chapters'),
    )
    Type = forms.TypedChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect, coerce=int)
    Description = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols':'10','class':'form-control'}),required=True)

    class Meta:
        model = Publications
        fields = ('Type' , 'Description')

class recognitions_form(forms.ModelForm):
    Description = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols':'10','class':'form-control'}),required=True)

    class Meta:
        model = Recognitions
        fields = ('Description',)
