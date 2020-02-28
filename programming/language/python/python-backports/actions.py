#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system("python -m compileall .")

def install():
    pisitools.insinto("/usr/lib/python2.7/site-packages/backports/", "__init__.py")
    pisitools.insinto("/usr/lib/python2.7/site-packages/backports/", "__init__.pyc")