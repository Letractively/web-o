from website.models import *
from django.contrib import admin

class PictureInLine(admin.TabularInline): # pragma: no cover
    model = Picture
    extra = 1

class NoticeAdmin(admin.ModelAdmin): # pragma: no cover
    inlines = [PictureInLine]
    list_display = ('title', 'notice_type', 'due_date')
    list_filter = ('notice_type', 'created')


for m in [PublicationTarget, PublicationAttach, Publication, Picture, MemberType, # pragma: no cover
          Member, Area, Technology, ProjectType, ProjectStatus, Project]:
    admin.site.register(m) # pragma: no cover

admin.site.register(Notice, NoticeAdmin) # pragma: no cover
