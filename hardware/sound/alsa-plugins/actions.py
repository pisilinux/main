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
    autotools.configure("--prefix=/usr \
        --sysconfdir=/etc \
        --enable-maemo-plugin")

def build():
    autotools.make()
    
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/etc/alsa/conf.d/98-maemo.conf")
    pisitools.domove("/etc/alsa/conf.d/99-pulseaudio-default.conf.example", "/usr/share/alsa/alsa.conf.d", "99-pulseaudio-default.conf")
    pisitools.dosym("/usr/share/alsa/alsa.conf.d/99-pulseaudio-default.conf", "/etc/alsa/conf.d/99-pulseaudio-default.conf")
    
    #shelltools.system("rm -v %s/etc/alsa/conf.d/98-maemo.conf" % get.installDIR())
    #shelltools.cd("%s" % get.installDIR())
    #shelltools.system("cp -r /etc/alsa/conf.d/99-pulseaudio-default.conf.example %s/usr/share/alsa/alsa.conf.d/99-pulseaudio-default.conf" % get.installDIR())
    #shelltools.system("ln -st  %s/etc/alsa/conf.d/ /usr/share/alsa/alsa.conf.d/99-pulseaudio-default.conf" % get.installDIR())

