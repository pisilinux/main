#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    #pisitools.dosed(".", "^(SUBDIRS =.*)tests(.*)$", "\\1\\2", filePattern="^Makefile.(am|in)", level=0)
    #autotools.autoreconf("-fiv")
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    options = "meson --prefix=/usr --libdir=lib \
                         -Denable-introspection=true \
              "
              
    if get.buildTYPE() == "emul32":
        options += "--libdir=lib32 .."
    
    shelltools.system(options)

def build():
    shelltools.cd("build")
    shelltools.system

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    if get.buildTYPE() == "emul32":
        #pisitools.removeDir("/usr/share/gtk-doc")
        return
    
        shelltools.cd("build")
        pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")
