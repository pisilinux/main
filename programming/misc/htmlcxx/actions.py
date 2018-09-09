#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    shelltools.export("LDFLAGS", "%s -lm" % get.LDFLAGS())
    autotools.autoreconf("-fiv")
    autotools.configure("--prefix=/usr")
   
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():  
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING")    
