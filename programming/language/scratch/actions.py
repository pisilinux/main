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
    pisitools.dosed("src/scratch", "-xshm ", "")
    # fix unused direct dependency analysis
    pisitools.dosed("src/plugins/unicode/Makefile", "gcc -shared", "gcc -Wl,-O1,--as-needed -shared")

def build():
    pisitools.cflags.add("-Wno-unused-result -Wno-parentheses -Wno-implicit-function-declaration")
    shelltools.system("make build")

def install():
    # install binary and additional files
    pisitools.insinto("/usr/bin/", "src/scratch")
    shelltools.chmod("%s/usr/bin/scratch" % get.installDIR(), 0755)
    pisitools.insinto("/usr/lib/scratch/", "Scratch.image")
    pisitools.insinto("/usr/lib/scratch/", "Scratch.ini")
    pisitools.insinto("/usr/share/applications/", "src/scratch.desktop")
    pisitools.insinto("/usr/share/mime/packages/", "src/scratch.xml")
    
    # install documentation files
    pisitools.dodoc("LICENSE*", "README*", "gpl*")
    shelltools.copytree("Help", "%s/usr/share/doc/scratch" % get.installDIR())
    
    #install man file
    pisitools.insinto("/usr/share/man/man1/", "src/man/scratch.1.gz")
    
    # install data files under share
    for dirs in ["Help", "locale", "Media", "Projects"]:
        shelltools.copytree(dirs, "%s/usr/share/scratch" % get.installDIR())
    
    # install plugins
    shelltools.copytree("Plugins", "%s/usr/lib/scratch" % get.installDIR())
    
    # install images
    shelltools.cd("src/icons")
    for dirs in ["32x32", "48x48", "128x128"]:
        pisitools.insinto("/usr/share/icons/hicolor/%s/apps" % dirs, "%s/*.*" % dirs)