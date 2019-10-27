 #!/usr/bin/python
# -*- coding: utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
     
    autotools.configure("--disable-static")
    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog","NOTICE")