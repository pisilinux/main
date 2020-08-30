#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="jedi-%s" % get.srcVERSION()

def setup():
    # install process needs some header files from
    # typeshed github repo. so we add that repo
    # and copy the header files to the corresponding path
    for files in ["../typeshed-jedi_v0.16.0/*"]:
        shelltools.copy("%s" % files,"jedi/third_party/typeshed")
    for files in ["../django-stubs-1.5.0/*"]:
        shelltools.copy("%s" % files,"jedi/third_party/django-stubs")

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.dodoc("LICENSE*")