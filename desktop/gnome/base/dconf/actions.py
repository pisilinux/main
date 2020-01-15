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
	
    shelltools.system(""" sed -i "s|link_whole: libdconf_common,|link_with: libdconf_common,|g" common/meson.build """)
	
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. --prefix=/usr --sysconfdir=/etc -Dwith-dbus-service-dir=/usr/share/dbus-1/services \
        -Dwith-dbus-system-service-dir=/usr/share/dbus-1/system-services -Dwith-gio-modules-dir=/usr/lib/gio/modules \
        -Denable-gtk-doc=false -Denable-man=true")
    
    
def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    
def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "NEWS", "README")

