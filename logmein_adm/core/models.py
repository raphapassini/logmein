from django.db import models


class Project(models.Model):
    name = models.CharField("Nome", max_length=255, )
    url = models.URLField('URL', )
    secret = models.CharField("Segredo", max_length=255, )

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.url)
