#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS='On' \
                            -DCMAKE_INSTALL_PREFIX='/usr' \
                            -DCPM_USE_LOCAL_PACKAGES='On' \
                            -DSIMDJSON_DEVELOPER_MODE='On' \
                            -DSIMDJSON_ALLOW_DOWNLOADS='Off' \
                        ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS*", "LICENSE*", "README*")
