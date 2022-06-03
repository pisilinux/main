#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir="pyalsaaudio-%s" % get.srcVERSION()

def build():
    shelltools.copytree("../pyalsaaudio-%s" % (get.srcVERSION().replace("_", "~")), "../pyalsaaudio-%s-py2" % get.srcVERSION())


    shelltools.cd("../pyalsaaudio-%s-py2" % get.srcVERSION())
    pythonmodules.compile()

    shelltools.cd("../pyalsaaudio-%s" % get.srcVERSION())
    pythonmodules.compile(pyVer="3")

def install():
    shelltools.cd("../pyalsaaudio-%s-py2" % get.srcVERSION())
    pythonmodules.install()

    shelltools.cd("../pyalsaaudio-%s" % get.srcVERSION())
    pythonmodules.install(pyVer="3")
