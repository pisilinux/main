#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    pisitools.dosed("astroid/__pkginfo__.py", "six~=[0-9.*]*", "six")
    pisitools.dosed("astroid/__pkginfo__.py", "wrapt~=[0-9.*]*", "wrapt")
    pisitools.dosed("astroid/__pkginfo__.py", "lazy_object_proxy==[0-9.*]*", "lazy_object_proxy")

def build():
    pythonmodules.compile(pyVer="3")


def install():
    pythonmodules.install(pyVer="3")
