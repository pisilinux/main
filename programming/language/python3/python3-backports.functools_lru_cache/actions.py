#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def build():
    python3modules.compile()

def install():
    python3modules.install()

    # Fix conflict with python3-backports_tarfile
    pisitools.remove("/usr/lib/python3.14/site-packages/backports/__init__.py")
    pisitools.remove("/usr/lib/python3.14/site-packages/backports/__pycache__/__init__.cpython-314.pyc")
