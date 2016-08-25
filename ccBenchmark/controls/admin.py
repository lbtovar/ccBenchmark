from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Benchmark, Section, Control, Project, Remediation


admin.site.register(Benchmark)
admin.site.register(Section, MPTTModelAdmin)
admin.site.register(Project)
admin.site.register(Control)
admin.site.register(Remediation)
