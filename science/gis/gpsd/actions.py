#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import scons
                                                                                                                                                  
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def build():
    scons.make( "prefix=/usr \
                 systemd=no \
                 libQgpsmm=no \
                 PYTHONPATH=/usr/bin/python")

def install():
    scons.install("--install-sandbox=%s" % get.installDIR())

    # We're using conf.d instead of sysconfig
    #pisitools.dosed("gpsd.hotplug.wrapper", "sysconfig\/", "conf.d/")

    # Install UDEV files
    pisitools.insinto("/lib/udev/rules.d", "gpsd.rules", "99-gpsd.rules")
    pisitools.dobin("gpsd.hotplug", "/lib/udev")
    #pisitools.dobin("gpsd.hotplug.wrapper", "/lib/udev")

    # Fix permissions
    #lsshelltools.chmod("%s/usr/lib/%s/site-packages/gps/gps.py" % (get.installDIR(), get.curPYTHON()))

    pisitools.dodoc("README", "TODO", "AUTHORS", "COPYING")
