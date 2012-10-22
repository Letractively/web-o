from django.test import TestCase
from django.http import Http404
from django.test.client import RequestFactory

from mock import Mock, patch

from website.models import Project, Member, Notice, Picture
from website.views import ProjectView, HomeView
from website.templatetags.custom_filters import areas, technologies

class ModelsTest(TestCase):
    def test_normalize(self):
        projects = Project.objects.all()
        for p in projects:
            norm_name = p.normalized_name()
            for c in norm_name:
                self.assertTrue(c.isalnum() or c in ['-', '_'])

    def test_complete_name(self):
        m = Member(first_name='a', last_name='b')
        self.assertEquals(m.complete_name(), 'a b')


    def test_notice_first_image(self):
        notice = Notice(title='title', content='content')
        notice.save()
        self.assertEquals(notice.first_image, None)
        picture = Picture.objects.create(notice=notice, image='')
        picture.save()
        self.assertEquals(Notice.objects.get(id=notice.id).first_image, picture.image)

class ViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def make_view_request(self, method, url, view, args=[], **kwargs):
        factory = self.factory.get if method == 'get' else self.factory.post
        request = factory(url)
        return view(request=request, args=args, kwargs=kwargs)

class HomeViewTest(ViewTest):

    def test_get(self):
        view = self.make_view_request('get', '/', HomeView)
        context = view.get_context_data()
        self.assertIn('notices', context)
        self.assertEquals(len(context['notices']), 2)

class ProjectViewTest(ViewTest):

    def test_get(self):
        projects = Project.objects.all()
        for p in projects:
            view, context = self.make_project_request(p.normalized_name())
            self.assertEquals(context['project'], p)
            view, context = self.make_project_request(p.normalized_name().lower())
            self.assertEquals(context['project'], p)

        with self.assertRaises(Http404):
            view = self.make_project_request('abc')
            view.get_context_data()

    def make_project_request(self, name):
        view = self.make_view_request('get', '/projects/%s' % name, ProjectView, [name])
        return view, view.get_context_data()

class CustomFiltersTest(TestCase):

    def test_areas(self):
        p1, p2, project = Mock(), Mock(), Mock()
        p1.description = 'a'
        p2.description = 'b'
        project.areas.all = Mock(return_value=[p1, p2])
        self.assertEquals(areas(project), 'a, b')

    def test_technologies(self):
        p1, p2, project = Mock(), Mock(), Mock()
        p1.description = 'a'
        p2.description = 'b'
        project.technologies.all = Mock(return_value=[p1, p2])
        self.assertEquals(technologies(project), 'a, b')
