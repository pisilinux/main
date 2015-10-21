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
    shelltools.system("PYTHON=/usr/bin/python2.7 HAVE_GCOV_FALSE='#' ./configure \
                          --disable-static \
                          --disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.domove("/usr/local/include/libaccounts-glib/*", "/usr/include/libaccounts-glib/")
    pisitools.domove("/usr/local/lib/*", "/usr/lib/")
    pisitools.domove("/usr/local/bin/*", "/usr/bin/")
    pisitools.domove("/usr/local/share/*", "/usr/share/")
    
    pisitools.removeDir("/usr/local")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
