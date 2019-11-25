 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
import os

NoStrip = ["/usr"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0755)

#def setup():
	#shelltools.system("mkdir -p build")
	#shelltools.cd("build")
	#shelltools.system("cmake -DBUILD_CGAME=OFF -DBUILD_SGAME=OFF -DOpenGL_GL_PREFERENCE=LEGACY ..")

#def build():
	#shelltools.cd("build")
	#cmaketools.make()

def install():
    #pisitools.insinto("/usr/share/pixmaps", "debian/unvanquished.png")
    #pisitools.dodoc("COPYING.txt")
    
    #shelltools.cd("build")
    #pisitools.insinto("/usr/lib/unvanquished", "daemon")
    #pisitools.insinto("/usr/lib/unvanquished", "daemonded")
    #pisitools.insinto("/usr/lib/unvanquished", "daemon-tty")
    #pisitools.insinto("/usr/lib/unvanquished", "irt_core-x86*.nexe")
    #pisitools.insinto("/usr/lib/unvanquished", "nacl_helper_bootstrap")
    #pisitools.insinto("/usr/lib/unvanquished", "nacl_loader")
    
    #shelltools.cd("../archlinux")
    #pisitools.insinto("/etc/conf.d", "unvanquished.conf")
    #pisitools.insinto("/etc/unvanquished", "configs/*")
    #pisitools.insinto("/usr/share/applications", "unvanquished.desktop")
    
    shelltools.system("mkdir -p bin")
    shelltools.system("unzip linux-amd64.zip -d bin")
    fixperms("bin")
    fixperms("pkg")
    pisitools.insinto("/usr/lib/unvanquished", "bin/*")
    pisitools.insinto("/usr/share/unvanquished/pkg", "pkg/*")

    #pisitools.dodoc("GPL.txt","COPYING.txt", "README.md")