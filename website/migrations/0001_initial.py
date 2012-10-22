# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PublicationTarget'
        db.create_table('website_publicationtarget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('website', ['PublicationTarget'])

        # Adding model 'Publication'
        db.create_table('website_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('objetive', self.gf('django.db.models.fields.TextField')()),
            ('authors_line', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('attach', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.PublicationTarget'], null=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Project'], null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Publication'])

        # Adding M2M table for field fudepan_authors on 'Publication'
        db.create_table('website_publication_fudepan_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publication', models.ForeignKey(orm['website.publication'], null=False)),
            ('member', models.ForeignKey(orm['website.member'], null=False))
        ))
        db.create_unique('website_publication_fudepan_authors', ['publication_id', 'member_id'])

        # Adding model 'MemberType'
        db.create_table('website_membertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('website', ['MemberType'])

        # Adding model 'Member'
        db.create_table('website_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('residence', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('linkedin_url', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('thesis_in_fudepan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.MemberType'], null=True)),
        ))
        db.send_create_signal('website', ['Member'])

        # Adding model 'ProjectType'
        db.create_table('website_projecttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('website', ['ProjectType'])

        # Adding model 'ProjectStatus'
        db.create_table('website_projectstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('website', ['ProjectStatus'])

        # Adding model 'Area'
        db.create_table('website_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('website', ['Area'])

        # Adding model 'Technology'
        db.create_table('website_technology', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('website', ['Technology'])

        # Adding model 'Project'
        db.create_table('website_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('objetive', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.ProjectType'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.ProjectStatus'], null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Project'])

        # Adding M2M table for field areas on 'Project'
        db.create_table('website_project_areas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['website.project'], null=False)),
            ('area', models.ForeignKey(orm['website.area'], null=False))
        ))
        db.create_unique('website_project_areas', ['project_id', 'area_id'])

        # Adding M2M table for field technologies on 'Project'
        db.create_table('website_project_technologies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['website.project'], null=False)),
            ('technology', models.ForeignKey(orm['website.technology'], null=False))
        ))
        db.create_unique('website_project_technologies', ['project_id', 'technology_id'])

        # Adding M2M table for field authors on 'Project'
        db.create_table('website_project_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['website.project'], null=False)),
            ('member', models.ForeignKey(orm['website.member'], null=False))
        ))
        db.create_unique('website_project_authors', ['project_id', 'member_id'])

        # Adding model 'ProjectsStatusData'
        db.create_table('website_projectsstatusdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('data', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('website', ['ProjectsStatusData'])

        # Adding model 'Notice'
        db.create_table('website_notice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('notice_type', self.gf('django.db.models.fields.CharField')(default='notice', max_length=20)),
        ))
        db.send_create_signal('website', ['Notice'])


    def backwards(self, orm):
        # Deleting model 'PublicationTarget'
        db.delete_table('website_publicationtarget')

        # Deleting model 'Publication'
        db.delete_table('website_publication')

        # Removing M2M table for field fudepan_authors on 'Publication'
        db.delete_table('website_publication_fudepan_authors')

        # Deleting model 'MemberType'
        db.delete_table('website_membertype')

        # Deleting model 'Member'
        db.delete_table('website_member')

        # Deleting model 'ProjectType'
        db.delete_table('website_projecttype')

        # Deleting model 'ProjectStatus'
        db.delete_table('website_projectstatus')

        # Deleting model 'Area'
        db.delete_table('website_area')

        # Deleting model 'Technology'
        db.delete_table('website_technology')

        # Deleting model 'Project'
        db.delete_table('website_project')

        # Removing M2M table for field areas on 'Project'
        db.delete_table('website_project_areas')

        # Removing M2M table for field technologies on 'Project'
        db.delete_table('website_project_technologies')

        # Removing M2M table for field authors on 'Project'
        db.delete_table('website_project_authors')

        # Deleting model 'ProjectsStatusData'
        db.delete_table('website_projectsstatusdata')

        # Deleting model 'Notice'
        db.delete_table('website_notice')


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
        'website.project': {
            'Meta': {'ordering': "['name']", 'object_name': 'Project'},
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Area']", 'symmetrical': 'False'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Member']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'objetive': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'attach': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'authors_line': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'fudepan_authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Member']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objetive': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Project']", 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.PublicationTarget']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'website.publicationtarget': {
            'Meta': {'ordering': "['description']", 'object_name': 'PublicationTarget'},
            'date': ('django.db.models.fields.DateField', [], {}),
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