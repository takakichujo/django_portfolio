from django.contrib import admin

# Register your models here.
from .models import Testlist
from .models import PrefectureMst

admin.site.register(Testlist)
admin.site.register(PrefectureMst)