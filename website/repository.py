from website.models import Project
import re

def find_project_ilike(expr):
    pattern = re.compile('^%s$' % expr.replace('-', '.'), re.IGNORECASE)
    for p in Project.objects.all():
        if pattern.match(p.name):
            return p
