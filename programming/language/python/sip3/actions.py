#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
WorkDir = "sip-%s" % get.srcVERSION()
py3dir = "python3.4"

def setup():
    shelltools.system("find . -type f -exec sed -i 's/Python.h/python3.4m\/Python.h/g' {} \;")

    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.run('configure.py \
                    -b /usr/bin \
                    -d /usr/lib/%s/site-packages/ \
                    -e /usr/include/%s/ \
                    CFLAGS="%s" CXXFLAGS="%s"' % (py3dir, py3dir, get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")

def build():

    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.make()

def install():

    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.rawInstall("DESTDIR=%s -C sipgen" % get.installDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/bin/sip", "sip3")

