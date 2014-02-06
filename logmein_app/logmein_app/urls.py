#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'logmein_app.views',
    url(r'^login/$', "logmein_login", name="logmein_login"),
)
