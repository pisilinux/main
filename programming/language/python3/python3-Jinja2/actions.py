#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

WorkDir = "Jinja2-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.insinto(examples, "examples/*")

    #Create docs with python-Sphinx
    #shelltools.cd("docs")
    #autotools.make("html")
    #shelltools.cd("..")
    #pisitools.dohtml("Jinja2-%s/docs/_build/html/*" % get.srcVERSION())
    pisitools.dodoc("CHANGES*", "README*")
