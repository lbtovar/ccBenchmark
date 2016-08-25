from django.contrib import admin

from .models import Benchmark, Section, Control, Project, Remediation

admin.site.register(Benchmark)
admin.site.register(Section)
admin.site.register(Project)
admin.site.register(Control)
admin.site.register(Remediation)
