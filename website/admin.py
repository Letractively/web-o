from website.models import *
from django.contrib import admin

class PictureInLine(admin.TabularInline): # pragma: no cover
    model = Picture
    extra = 1

class NoticeAdmin(admin.ModelAdmin): # pragma: no cover
    inlines = [PictureInLine]
    list_display = ('title', 'notice_type', 'due_date')
    list_filter = ('notice_type', 'created')

class PublicationAttachInline(admin.TabularInline):
    model = PublicationAttach
    extra = 1        

class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationAttachInline]
    list_display = ('title', 'project')
    list_filter = ('project',)
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        pub = form.save(commit=False)
        for i in instances:
            if not i.title:
                title = '%s - %s' % (pub.project.name, pub.title[:100])
                i.title = title
                i.save()
        formset.save_m2m()

for m in [PublicationTarget,  Picture, PublicationAttach, MemberType, # pragma: no cover
          Member, Area, Technology, ProjectType, ProjectStatus, Project]:
    admin.site.register(m) # pragma: no cover

admin.site.register(Publication, PublicationAdmin)
admin.site.register(Notice, NoticeAdmin)
