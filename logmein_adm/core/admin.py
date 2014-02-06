import datetime
import hashlib
from django.contrib import admin
from django.conf.urls import patterns, url
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from .models import Project


def login_button(obj):
    return "<a href='%s?pk=%d' target='_blank'>Efetuar Login</a>" % \
        (reverse_lazy('admin:project_login'), obj.pk)
login_button.short_description = 'Login'
login_button.allow_tags = True


def get_token(secret):
        now = datetime.datetime.utcnow()
        second = now.second
        token_str = ''.join(
            [secret, now.strftime("%Y%m%d%H%M"), str(second), ])
        token = hashlib.sha224(token_str).hexdigest()
        return token


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', login_button)

    def get_urls(self):
        urls = super(ProjectAdmin, self).get_urls()
        custom_urls = patterns(
            '',
            url(r'^project_login/$', self.project_login, name="project_login"),
        )
        return custom_urls + urls

    def project_login(self, request):
        try:
            project = Project.objects.get(pk=request.GET.get('pk'))
        except Project.DoesNotExist:
            return reverse_lazy('admin:project')

        token = get_token(secret=project.secret)
        url = "%s?token=%s" % (project.url, token)
        return redirect(url)

admin.site.register(Project, ProjectAdmin)
