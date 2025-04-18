#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def build():
    shelltools.system("python3 -m build --wheel --no-isolation")
    # python3modules.compile()

def install():
    shelltools.system("python3 -m installer --destdir=%s dist/*.whl" % get.installDIR())
    # python3modules.install()
    pisitools.insinto("/usr/lib/python3.11/site-packages/jaraco/text", "jaraco/text/Lorem ipsum.txt")

    # pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README")
