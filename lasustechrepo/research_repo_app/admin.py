from django.contrib import admin
from .models import Thesis, ResearchPaper, ResearchData
# Register your models here.


admin.site.register(Thesis)
admin.site.register(ResearchPaper)
admin.site.register(ResearchData)