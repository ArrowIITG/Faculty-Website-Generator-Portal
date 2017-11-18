from django.contrib import admin

# Register your models here.
from .models import About_us , Teaching , Students , Projects , Publications , Recognitions,Mail

admin.site.register(About_us);
admin.site.register(Teaching);
admin.site.register(Students);
admin.site.register(Projects);
admin.site.register(Publications);
admin.site.register(Recognitions);
admin.site.register(Mail);
