# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        import re
        
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        for project in orm['website.Project'].objects.all():
            description = project.type.description.lower() if project.type else ''
            if re.search('research', description) is not None or \
                   re.search('invest', description) is not None:
                project.sort_order = 100
            if project.sort_order is None and \
                   re.search('framework', description) is not None:
                project.sort_order = 200
            if project.sort_order is None and \
                   (re.search('application', description) is not None or \
                    re.search('aplica', description) is not None):
                project.sort_order = 300
            if project.sort_order is None and \
                re.search('libr', description) is not None:
                project.sort_order = 400
            if project.sort_order is None:
                project.sort_order = 500
            project.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        for project in orm['website.Project'].objects.all():
            project.sort_order = None
            project.save()

    models = {
        'website.area': {
            'Meta': {'ordering': "['description']", 'object_name': 'Area'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.member': {
            'Meta': {'ordering': "['first_name']", 'object_name': 'Member'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'linkedin_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'residence': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'thesis_in_fudepan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.MemberType']", 'null': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'website.membertype': {
            'Meta': {'ordering': "['description']", 'object_name': 'MemberType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.notice': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Notice'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notice_type': ('django.db.models.fields.CharField', [], {'default': "'notice'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'website.picture': {
            'Meta': {'object_name': 'Picture'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'notice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Notice']"})
        },
        'website.project': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Project'},
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Area']", 'symmetrical': 'False'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Member']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'objetive': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.ProjectStatus']", 'null': 'True', 'blank': 'True'}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['website.Technology']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.ProjectType']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'website.projectsstatusdata': {
            'Meta': {'object_name': 'ProjectsStatusData'},
            'data': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        'website.projectstatus': {
            'Meta': {'ordering': "['description']", 'object_name': 'ProjectStatus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.projecttype': {
            'Meta': {'ordering': "['description']", 'object_name': 'ProjectType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.publication': {
            'Meta': {'ordering': "['title']", 'object_name': 'Publication'},
            'authors_line': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fudepan_authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Member']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objetive': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Project']", 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.PublicationTarget']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'website.publicationattach': {
            'Meta': {'object_name': 'PublicationAttach'},
            'attach': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Publication']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        'website.publicationtarget': {
            'Meta': {'ordering': "['description']", 'object_name': 'PublicationTarget'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.technology': {
            'Meta': {'ordering': "['description']", 'object_name': 'Technology'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['website']
    symmetrical = True
