#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def build():
    shelltools.system('sed -i "s/flit_core<4/flit_core<5/" pyproject.toml')
    python3modules.compile(pyVer="3")
    # build documentation
    #shelltools.cd("docs")
    autotools.make("-C docs PYTHONPATH=$(pwd)/src SPHINXBUILD=sphinx-build ")

def install():
    python3modules.install(pyVer="3")
    pisitools.dodoc("LICENSE*")
    # pisitools.dohtml("docs/_build/html/*")
