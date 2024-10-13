#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules

# shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","20.0.27")

def build():
    python3modules.compile()

def install():
    python3modules.install()
