from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.utils import timezone


# Create your models here.

class About_us(models.Model):
    username = models.OneToOneField(User , on_delete=models.CASCADE,primary_key=True,related_name="xyz",)
    slug = models.SlugField(null=True, blank=True , unique=True)
    Upload_Profile_Pic = models.ImageField(upload_to='uploads' ,null=True , blank=True)
    Department = models.CharField(max_length=200)
    Departmental_post = models.CharField(max_length=200)
    Room_no = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    Research_interest = models.TextField()
    primary_Research_group = models.TextField()

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username.username

    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug })


class Teaching(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Teach" )
    slug = models.SlugField(null=True, blank=True , unique=True)
    YEAR_CHOICES = []
    for r in range(1950, (datetime.datetime.now().year+1)):
        s = str(r)+"-"+str(r+1)
        YEAR_CHOICES.append((s,s))

    year = models.CharField(max_length=255 , choices=YEAR_CHOICES , default='select')
    semester = models.NullBooleanField('semester:' , null=True , blank=True)
    Subject_code = models.CharField(max_length=10)
    Subject = models.CharField(max_length=200)
    Partners = models.CharField(max_length=200 , default=None)

    def __str__(self):
        return self.username.username

    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug })

CATEGORY = (
    (0 , 'M.Tech. Students Ongoing'),
    (1 , 'M.Tech. Students Completed'),
    (2 , 'Ph.D. Students Continuing'),
    (3 , 'Ph.D. Students Completed'),
)

class Students(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Student" )
    slug = models.SlugField(null=True, blank=True , unique=True)
    Student_name = models.CharField(max_length=100)
    Student_category = models.IntegerField( choices=CATEGORY , default=None)
    Thesis_title = models.CharField(max_length=3000)
    Supervisors = models.CharField(max_length=3000)

    def __str__(self):
        return self.username.username

    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug })


class Projects(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="projects" )
    slug = models.SlugField(null=True, blank=True , unique=True)
    Project_Type =  models.NullBooleanField('Project_Type:' , null=True, blank=True )
    Project_title = models.CharField(max_length=5000, default=None)
    PI = models.CharField(max_length=2000, default=None)
    co_PI =  models.CharField(max_length=2000, null=True, blank=True , default=None)
    Funding_Agency = models.CharField(max_length=2000 ,  null=True, blank=True ,default=None)
    START_YEAR_CHOICES = []
    for r in range(1950, (datetime.datetime.now().year+1)):
        s = str(r)+"-"+str(r+1)
        START_YEAR_CHOICES.append((s,s))

    Start_year = models.CharField(max_length=255 , choices=START_YEAR_CHOICES , default=datetime.datetime.now().year )
    END_YEAR_CHOICES = []
    for r in range(1950, (datetime.datetime.now().year+1)):
        END_YEAR_CHOICES.append((str(r) ,str(r)))

    End_Year = models.CharField(max_length=4 , choices=END_YEAR_CHOICES , null=True , blank=True)

    def __str__(self):
        return self.username.username

    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug })


class Publications(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Publications" )
    slug = models.SlugField(null=True, blank=True , unique=True)
    Description = models.TextField()
    Type = models.BooleanField('Type:')


    def __str__(self):
        return self.username.username

class Recognitions(models.Model):
    username = models.ForeignKey(User , on_delete=models.CASCADE  , related_name="Recognitions" )
    slug = models.SlugField(null=True, blank=True , unique=True)
    Description = models.TextField()

    def __str__(self):
        return self.username.username
