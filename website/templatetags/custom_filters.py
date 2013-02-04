from django import template

register = template.Library()

@register.filter
def areas(project):
    return ', '.join([a.description for a in project.areas.all()])

@register.filter
def technologies(project):
    return ', '.join([a.description for a in project.technologies.all()])
