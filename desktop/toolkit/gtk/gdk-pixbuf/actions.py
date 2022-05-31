#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
  options = "-Dbuiltin_loaders=png \
            "
  if get.buildTYPE()=="emul32":
      options += "-Dintrospection=disabled \
                  -Dinstalled_tests=false \
                  --bindir=/usr/bin32"
  else:
      options += "-Dintrospection=enabled -Dgtk_doc=true"

  mesontools.configure(options)

def build():
     mesontools.build()

def install():
    mesontools.install()
    if get.buildTYPE() == "emul32":
        pisitools.domove("/usr/bin32/gdk-pixbuf-query-loaders", "/usr/bin", "gdk-pixbuf-query-loaders-32")
        pisitools.removeDir("/usr/bin32")
        return
    pisitools.dosym("/usr/bin/gdk-pixbuf-query-loaders", "/usr/bin/gdk-pixbuf-query-loaders-64")
    pisitools.dodoc("COPYING", "README.md")
