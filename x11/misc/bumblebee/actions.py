#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("\
                         CONF_DRIVER=nvidia \
                         CONF_DRIVER_MODULE_NVIDIA=nvidia \
                         CONF_LDPATH_NVIDIA=/usr/lib/nvidia-current:/usr/lib32/nvidia-current \
                         CONF_MODPATH_NVIDIA=//usr/lib/nvidia-current,/usr/lib/xorg/modules \
                         CONF_PRIMUS_LD_PATH=/usr/lib/primus:/usr/lib32/primus \
                         CONF_BRIDGE=primus \
                         --with-udev-rules=/lib/udev/rules.d/ \
                         --without-pidfile \
                         ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
