#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")
    autotools.configure("--with-drivers=all \
                         --enable-nls \
                         --disable-rpath \
                         --disable-lockdev \
                         --disable-resmgr \
                         --disable-ttylock \
                         --disable-baudboy \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s udevscriptdir=/lib/udev" % get.installDIR())

#    HAL_FDI="usr/share/hal/fdi/information/20thirdparty/10-camera-libgphoto2.fdi"
    UDEV_RULES="lib/udev/rules.d/40-libgphoto2.rules"
    HWDB_RULES="lib/udev/rules.d/20-libgphoto2.hwdb"
    CAM_LIST="usr/lib/libgphoto2/print-camera-list"
    CAM_LIBS="usr/lib/libgphoto2/%s" % get.srcVERSION()

    # Create hal directory
#    pisitools.dodir(shelltools.dirName(HAL_FDI))

    # Export the necessary env variables
    shelltools.export("CAMLIBS", "%s/%s" % (get.installDIR(), CAM_LIBS))
    shelltools.export("LIBDIR", "%s/usr/lib/" % get.installDIR())
    shelltools.export("LD_LIBRARY_PATH", "%s/usr/lib/" % get.installDIR())

    # Generate HAL FDI file
#    f = open(os.path.join(get.installDIR(), HAL_FDI), "w")
#    f.write(os.popen("%s/%s hal-fdi" % (get.installDIR(), CAM_LIST)).read())
#    f.close()

    # Generate UDEV rule which will replace the HAL FDI when HAL is deprecated
    pisitools.dodir("/lib/udev/rules.d")
    f = open(os.path.join(get.installDIR(), UDEV_RULES), "w")
    f.write(os.popen("%s/%s udev-rules version 201" % (get.installDIR(), CAM_LIST)).read())
    f.close()

    f = open(os.path.join(get.installDIR(), HWDB_RULES), "w")
    f.write(os.popen("%s/%s hwdb" % (get.installDIR(), CAM_LIST)).read())
    f.close()

    pisitools.removeDir("/usr/share/doc/libgphoto2_port")
    pisitools.removeDir("/usr/share/libgphoto2_port")

    # Remove circular symlink
    #pisitools.remove("/usr/include/gphoto2/gphoto2")

    pisitools.dodoc("HACKING.md", "MAINTAINERS", "TESTERS")

