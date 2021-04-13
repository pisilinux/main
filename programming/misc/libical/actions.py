#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
                          -DCMAKE_BUILD_TYPE=Release   \
                          -DSHARED_ONLY=yes            \
                          -DICAL_BUILD_DOCS=true       \
                          -DGOBJECT_INTROSPECTION=true \
                          -DICAL_GLIB_VAPI=true")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
