#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	mesontools.configure("-DBUILD_MANS=false \
		                  -DBUILD_HTML_MANS=false")

def build():
    mesontools.build()

def install():
    shelltools.cd("build")
    pisitools.dobin("ping/ping")

    for app in ["clockdiff", "arping", "tracepath"]:
        pisitools.dosbin(app)

    # We will not need these if we set cap on postInstall like Fedora
    shelltools.chmod("%s/usr/bin/ping" % get.installDIR(), 04711)
    #shelltools.chmod("%s/usr/bin/ping6" % get.installDIR(), 04711)

    pisitools.dodoc("../README.md")
