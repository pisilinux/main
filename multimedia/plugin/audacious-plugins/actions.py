#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# if pisi can't find source directory, see /var/pisi/__package_name__/work/ and:
# WorkDir="__package_name__-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    autotools.rawConfigure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s"%get.installDIR())
    
