#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "png_check_sig", "png_sig_cmp")
    pisitools.dosed("configure.ac", "FTGL.h", "ftgl.h")
    autotools.autoreconf("-vfi")
    autotools.configure("--sysconfdir=/etc \
		                 --mandir=/usr/share/man \
		                 --disable-games \
		                 --enable-automakedefaults \
		                 --disable-uninstall")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")

    #We better cleanup
    pisitools.removeDir("/usr/share/armagetronad/desktop")
    shelltools.chmod("%s/etc/armagetronad/rc.config" % get.installDIR(), 0644)
    
    pisitools.dodir("/usr/share/armagetronad/moviepack")
    shelltools.copy("moviepack/*", "%s/usr/share/armagetronad/moviepack" % get.installDIR())
    
    pisitools.dodir("/usr/share/armagetronad/moviesounds")
    shelltools.copy("moviesounds/*", "%s/usr/share/armagetronad/moviesounds" % get.installDIR())
