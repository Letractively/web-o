from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from website.models import Project, Member, Publication, ProjectsStatusData, \
                            Notice, PublicationAttach
from website.repository import find_project_ilike
import datetime
import simplejson

#GenericsViews:
class FudepanView(TemplateView):
    def get_context_data(self, **kwargs):
        context = dict()
        context['notices'] = Notice.objects.all()[:2]
        context['current'] = getattr(self, 'current', None)
        return context

class Error500(FudepanView):
    template_name = '500.html'

class Error404(FudepanView):
    template_name = '404.html'

class GenericInicioView(FudepanView):
    current = 'INICIO'

class GenericInstitucionalView(FudepanView):
    current = 'INSTITUCIONAL'

class GenericColaboradoresView(FudepanView):
    current = 'COLABORADORES'

class GenericProyectosView(FudepanView):
    current = 'PROYECTOS'

class GenericInternalView(FudepanView):
    current = 'INTERNAL'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):  #pragma: no cover
        return super(FudepanView, self).dispatch(*args, **kwargs)

#website views:
class HomeView(GenericInicioView):
    template_name = 'website/home.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(GenericInicioView, self).get_context_data(**kwargs)
        return context

class ContactoView(FudepanView):
    current = 'CONTACTO'
    template_name = 'website/contacto.html'

class QueHacemosView(FudepanView):
    current = 'QUE HACEMOS'
    template_name = 'website/que_hacemos.html'

class ComoColaborarView(FudepanView):
    current = 'COMO COLABORAR'
    template_name = 'website/como_colaborar.html'

class QuienesSomosView(GenericInstitucionalView):
    template_name = 'website/quienes_somos.html'

    def get_context_data(self, **kwargs):
        context = super(GenericInstitucionalView, self).get_context_data(**kwargs)
        context['members'] = Member.objects.exclude(image__isnull=True).exclude(image__exact='')
        return context

class NuestrosLogrosView(GenericInstitucionalView):
    template_name = 'website/nuestros_logros.html'

class ColaboradoresView(GenericColaboradoresView):
    template_name = 'website/colaboradores.html'

    def get_context_data(self, **kwargs):
        context = super(GenericColaboradoresView, self).get_context_data(**kwargs)
        context['directores'] = Member.objects.filter(type__description='Director')
        context['profesionales'] = Member.objects.filter(type__description='Profesionales / Voluntarios')
        context['investigadores'] = Member.objects.filter(type__description='Investigadores y Docentes Asociados')
        context['coord_general'] = Member.objects.filter(type__description='Coordinador General')
        context['coord_regional'] = Member.objects.filter(type__description='Coordinador Regional')
        context['estudiantes'] = Member.objects.filter(type__description='Estudiantes Universitarios')
        context['ex_colaboradores'] = Member.objects.filter(type__description='Ex colaboradores')
        return context

class MemberView(GenericColaboradoresView):
    template_name = 'website/member.html'

    def get_context_data(self, **kwargs):
        context = super(GenericColaboradoresView, self).get_context_data(**kwargs)
        try:
            id = int(self.args[0])
        except:
            raise Http404()
        member = get_object_or_404(Member, id=id)
        context['member'] = member
        context['projects'] = Project.objects.filter(authors=member)
        context['publications'] = Publication.objects.filter(fudepan_authors=member)
        return context

class PublicationsView(GenericProyectosView):
    template_name = 'website/publications.html'

    def get_context_data(self, **kwargs):
        context = super(GenericProyectosView, self).get_context_data(**kwargs)
        context['publications'] = Publication.objects.all().order_by('-date')
        return context

class PublicationView(GenericProyectosView):
    template_name = 'website/publication.html'

    def get_context_data(self, **kwargs):
        try:
            id = int(self.args[0])
        except:
            raise Http404()
        context = super(GenericProyectosView, self).get_context_data(**kwargs)
        
        publication = get_object_or_404(Publication, id=id)
        context['publication'] = publication
        context['attachments'] = PublicationAttach.objects.filter(publication=publication)
        return context

class ProjectsView(GenericProyectosView):
    template_name = 'website/projects.html'

    def get_context_data(self, **kwargs):
        context = super(GenericProyectosView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

class ProjectView(GenericProyectosView):
    template_name = 'website/project.html'

    def get_context_data(self, **kwargs):
        context = super(GenericProyectosView, self).get_context_data(**kwargs)
        p = find_project_ilike(self.args[0])
        if p:
            context['project'] = p
            context['related_publication'] = Publication.objects.filter(project=p)
            return context
        else:
            raise Http404

def notices(request, id=None):
    if id is not None:
        obj = get_object_or_404(Notice, id=id)
    else:
        obj = Notice.objects.latest('created')
    
    notices = Notice.objects.all()
    return render(
        request,
        'website/notices.html',
        {
            'notices':notices,
            'obj': obj
        }
    )
