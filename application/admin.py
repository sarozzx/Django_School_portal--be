from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Assignment, GAssignment,checkassignment,feed,assign,assignsubmit

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Assignment)
admin.site.register(GAssignment)
admin.site.register(checkassignment)
admin.site.register(feed)
admin.site.register(assign)
admin.site.register(assignsubmit)
