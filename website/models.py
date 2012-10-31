from django.db import models
from fudepan import settings
import os

class PublicationTarget(models.Model):
    class Meta:
        ordering = ['description']

    description = models.CharField(max_length=300)

    def __unicode__(self):
        return self.description

class PublicationAttach(models.Model):
    attach = models.FileField(upload_to='publications')
    title = models.CharField(max_length=300, null=True, blank=True)
    publication = models.ForeignKey('Publication')

    def __unicode__(self):
        return self.title or self.attach.name 

class Publication(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=300)
    objetive = models.TextField()
    authors_line = models.CharField(max_length=500)
    date = models.DateField(null=True, blank=True)
    target = models.ForeignKey(PublicationTarget, null=True)
    project = models.ForeignKey('Project', null=True, blank=True)
    fudepan_authors = models.ManyToManyField('Member')

    def __unicode__(self):
        return self.title

class MemberType(models.Model):
    class Meta:
        ordering = ['description']

    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description


class Member(models.Model):
    class Meta:
        ordering = ['first_name']

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50, null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    residence = models.CharField(max_length=50, null=True, blank=True)
    university = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="users", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    thesis_in_fudepan = models.BooleanField(default=False)
    type = models.ForeignKey(MemberType, null=True)

    def complete_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class ProjectType(models.Model):
    class Meta:
        ordering = ['description']

    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description


class ProjectStatus(models.Model):
    class Meta:
        ordering = ['description']

    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description


class Area(models.Model):
    class Meta:
        ordering = ['description']

    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description


class Technology(models.Model):
    class Meta:
        ordering = ['description']

    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description


class Project(models.Model):
    class Meta:
        ordering = ['sort_order']

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    objetive = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    type = models.ForeignKey(ProjectType, null=True, blank=True)
    status = models.ForeignKey(ProjectStatus, null=True, blank=True)
    sort_order = models.PositiveIntegerField(default=500)

    areas = models.ManyToManyField(Area)
    technologies = models.ManyToManyField(Technology, blank=True, null=True)
    authors = models.ManyToManyField(Member)

    def normalized_name(self):
        norm = self.name
        for c in [',', '&', ' ', '-', '/']:
            norm = norm.replace(c, '-')
        return norm

    def __unicode__(self):
        return self.name


class ProjectsStatusData(models.Model):
    type = models.CharField(max_length=300, null=True, blank=True)
    data = models.TextField()
    timestamp = models.DateTimeField()


class Picture(models.Model):
    image = models.ImageField(upload_to='pictures')
    caption = models.CharField(max_length=200, null=True, blank=True)
    notice = models.ForeignKey('website.Notice')

    def __unicode__(self):
        return self.image


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True, editable=False)
    due_date = models.DateField(null=True, blank=True)
    notice_type = models.CharField(
        max_length=20,
        choices=(
            ('notice', 'Notices'),
            ('event', 'Events'),
            ('course', 'Course'),
         ),
         default='notice'
    )

    class Meta:
        ordering = ['-created']

    @property
    def first_image(self):
        try:
            image = self.picture_set.all()[0].image
        except Exception:
            #could raise any of DoesNotExist or AttributeError I don't care.
            image = None
        return image

    @models.permalink
    def get_absolute_url(self):
        return ('notice', [self.pk])

    def __unicode__(self):
        return self.title

