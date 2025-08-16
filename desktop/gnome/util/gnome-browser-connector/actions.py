#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    # Fixup for Python version
    # Pisi Linux links main Python executable to Python2, which causes
    # issues with the connector and its host process
    shelltools.system("""sed -i -e '/#!/s/python/python3/' %s/usr/bin/gnome-browser-connector*""" % get.installDIR())

    pisitools.dodoc("NEWS", "LICENSE*")
