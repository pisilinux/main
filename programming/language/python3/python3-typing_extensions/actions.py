#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.system("PYTHONPATH=flit_core python3 -m flit build --format wheel")

def install():
    shelltools.system("PIP_CONFIG_FILE=/dev/null pip3 install --isolated --root=%s --ignore-installed --no-deps dist/*.whl" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
