#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'logmein.views',
    url(r'^login/$', "logmein_login", name="logmein_login"),
)
